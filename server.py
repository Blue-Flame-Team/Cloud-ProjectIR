import os
import sys
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from unittest.mock import MagicMock
sys.modules['sklearn'] = MagicMock()

import Core
sys.modules['core'] = Core
from Core import data_loader
sys.modules['Load'] = data_loader

from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from Core.text_processor import TextProcessor
from Core.indexer import Indexer
from Core.search_engine import SearchEngine
from Core.data_loader import DataLoader
import nltk

try:
    import ssl
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

def _patched_vectorize_query(self, query_text):
    res = self.processor.preprocessing_steps(query_text)
    if not res or 'stemming' not in res:
        return {}
    clean_query_tokens = res['stemming']
    query_vector = {}
    if not clean_query_tokens:
        return query_vector
    token_counts = {}
    for word in clean_query_tokens:
        token_counts[word] = token_counts.get(word, 0) + 1
    vector_length = float(len(clean_query_tokens))
    for word, count in token_counts.items():
        if word in self.indexer.idf_cache:
            tf = count / vector_length
            idf = self.indexer.idf_cache[word]
            query_vector[word] = tf * idf
    return query_vector

SearchEngine._vectorize_query = _patched_vectorize_query

app = Flask(__name__)
dl = DataLoader()
tp = TextProcessor()
idx = Indexer()

base_dir = os.path.dirname(os.path.abspath(__file__))
docs_path = os.path.join(base_dir, 'Data')

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["ir_search_engine"]
collection = db["documents"]

all_docs = {}
engine = SearchEngine(idx, tp)

def rebuild_index():
    global all_docs, engine, idx, tp
    idx = Indexer()
    all_docs.clear()
    processed_docs = {}
    
    docs_cursor = collection.find()
    for doc in docs_cursor:
        d_id = str(doc["_id"])
        text = doc.get("content", "")
        all_docs[d_id] = text
        res = tp.preprocessing_steps(text)
        if res and 'stemming' in res:
            processed_docs[d_id] = res['stemming']
            
    idx.build_index(processed_docs)
    idx.compute_tf_idf()
    engine = SearchEngine(idx, tp)

def init_db():
    retries = 10
    while retries > 0:
        try:
            client.admin.command('ping')
            if collection.count_documents({}) == 0:
                if os.path.exists(docs_path):
                    seed_docs = dl.load_documents(docs_path)
                    for doc_id, text in seed_docs.items():
                        collection.insert_one({"content": text})
            rebuild_index()
            logger.info("Successfully connected and initialized DB")
            break
        except Exception as e:
            retries -= 1
            logger.warning(f"Waiting for MongoDB... {e}")
            time.sleep(3)

init_db()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    try:
        query = request.args.get("q", "")
        if not query:
            return render_template("index.html")
        res = engine.search(query, top_k=20)
        data = []
        for d_id, score in res:
            snip = all_docs.get(d_id, "")
            if len(snip) > 150:
                snip = snip[:150] + "..."
            data.append({"doc_id": d_id, "score": score, "snippet": snip})
        logger.info(f"Search query '{query}' yielded {len(data)} results.")
        return render_template("results.html", query=query, results=data)
    except Exception as e:
        logger.error(f"Error during search: {e}")
        return "Internal Server Error", 500

@app.route("/docs", methods=["GET"])
def list_docs():
    try:
        docs = list(collection.find())
        return render_template("docs_list.html", docs=docs)
    except Exception as e:
        logger.error(f"Error listing documents: {e}")
        return "Internal Server Error", 500

@app.route("/docs/create", methods=["GET", "POST"])
def create_doc():
    try:
        if request.method == "POST":
            content = request.form.get("content", "")
            if content:
                collection.insert_one({"content": content})
                rebuild_index()
                logger.info("Document created successfully.")
                return redirect(url_for("list_docs"))
        return render_template("doc_form.html", doc=None)
    except Exception as e:
        logger.error(f"Error creating document: {e}")
        return "Internal Server Error", 500

@app.route("/docs/edit/<doc_id>", methods=["GET", "POST"])
def edit_doc(doc_id):
    try:
        doc = collection.find_one({"_id": ObjectId(doc_id)})
        if request.method == "POST":
            content = request.form.get("content", "")
            if content:
                collection.update_one({"_id": ObjectId(doc_id)}, {"$set": {"content": content}})
                rebuild_index()
                logger.info(f"Document {doc_id} updated successfully.")
                return redirect(url_for("list_docs"))
        return render_template("doc_form.html", doc=doc)
    except Exception as e:
        logger.error(f"Error editing document {doc_id}: {e}")
        return "Internal Server Error", 500

@app.route("/docs/delete/<doc_id>", methods=["POST"])
def delete_doc(doc_id):
    try:
        collection.delete_one({"_id": ObjectId(doc_id)})
        rebuild_index()
        logger.info(f"Document {doc_id} deleted successfully.")
        return redirect(url_for("list_docs"))
    except Exception as e:
        logger.error(f"Error deleting document {doc_id}: {e}")
        return "Internal Server Error", 500

@app.route("/api", methods=["GET"])
def api_docs():
    return render_template("api_docs.html")

@app.route("/api/docs", methods=["GET"])
def api_list_docs():
    try:
        docs = list(collection.find())
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        return jsonify({"status": "success", "data": docs}), 200
    except Exception as e:
        logger.error(f"API Error listing documents: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/docs/<doc_id>", methods=["GET"])
def api_get_doc(doc_id):
    try:
        doc = collection.find_one({"_id": ObjectId(doc_id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return jsonify({"status": "success", "data": doc}), 200
        return jsonify({"status": "error", "message": "Document not found"}), 404
    except Exception as e:
        logger.error(f"API Error getting document: {e}")
        return jsonify({"status": "error", "message": "Invalid ObjectId or Server Error"}), 500

@app.route("/api/docs", methods=["POST"])
def api_create_doc():
    try:
        data = request.get_json()
        if not data or "content" not in data:
            return jsonify({"status": "error", "message": "Content is required in JSON body"}), 400
        result = collection.insert_one({"content": data["content"]})
        rebuild_index()
        return jsonify({"status": "success", "message": "Document created", "id": str(result.inserted_id)}), 201
    except Exception as e:
        logger.error(f"API Error creating document: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/docs/<doc_id>", methods=["PUT"])
def api_update_doc(doc_id):
    try:
        data = request.get_json()
        if not data or "content" not in data:
            return jsonify({"status": "error", "message": "Content is required in JSON body"}), 400
        
        result = collection.update_one({"_id": ObjectId(doc_id)}, {"$set": {"content": data["content"]}})
        if result.matched_count == 0:
            return jsonify({"status": "error", "message": "Document not found"}), 404
            
        rebuild_index()
        return jsonify({"status": "success", "message": "Document updated"}), 200
    except Exception as e:
        logger.error(f"API Error updating document: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/docs/<doc_id>", methods=["DELETE"])
def api_delete_doc(doc_id):
    try:
        result = collection.delete_one({"_id": ObjectId(doc_id)})
        if result.deleted_count == 0:
            return jsonify({"status": "error", "message": "Document not found"}), 404
            
        rebuild_index()
        return jsonify({"status": "success", "message": "Document deleted"}), 200
    except Exception as e:
        logger.error(f"API Error deleting document: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

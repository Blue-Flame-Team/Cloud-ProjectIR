import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.stem.isri import ISRIStemmer
from Load import DataLoader 

class TextProcessor:
    def __init__(self):
        self.stop_words_english = set(stopwords.words('english'))
        self.stop_words_arabic = set(stopwords.words('arabic'))

        self.stemmer_multi = SnowballStemmer("english") 
        self.stemmer_ar = ISRIStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        if not text: return ""
        
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'\@\w+|\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
        
        return " ".join(text.split())

    def preprocessing_steps(self, text):
        cleaned_data = self.clean_text(text)
        if not cleaned_data: return None 
        
        tokens = word_tokenize(cleaned_data)
        
        remove_stop = [w for w in tokens if w.lower() not in self.stop_words_english and w not in self.stop_words_arabic]
        
        case_folding = [w.lower() for w in remove_stop]
        
        lemmatization = [self.lemmatizer.lemmatize(w, pos='n') for w in case_folding]
        lem_final = [self.lemmatizer.lemmatize(w, pos='v') for w in lemmatization]

        stemmed = []
        for w in lem_final:
            if re.search(r'[\u0600-\u06FF]', w):
                stemmed.append(self.stemmer_ar.stem(w))
            else:
                stemmed.append(self.stemmer_multi.stem(w))

        return {
            "original_data": text,
            "cleaned_data": cleaned_data,
            "tokenization_result": tokens,
            "stopping": remove_stop,
            "case_folding": case_folding,
            "lemmatization": lem_final,
            "stemming": stemmed
        }

if __name__ == "__main__":
    loader = DataLoader()
    processor = TextProcessor()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    documents_path = os.path.join(current_dir, "IR project", "documents")
    training_path = os.path.join(current_dir, "IR project", "archive", "twitter_training.csv")
    validation_path = os.path.join(current_dir, "IR project", "archive", "twitter_validation.csv")

    def display_results(title, data_source, limit=5):
        
        
        count = 0
        for key, content in data_source.items():
            if count >= limit: break
            
            result = processor.preprocessing_steps(content)
            if not result: continue 
            
            print(f"Source: {key}")
            print(f"ORIGINAL: {result['original_data'][:100]}...")
            print("." * 30)
            print(f"[1] CLEAN : {result['cleaned_data'][:80]}...")
            print(f"[2] TOKENS:  {result['tokenization_result'][:12]}")
            print(f"[3] Stopping_result: {result['stopping'][:12]}")
            print(f"[4] Casing_result:  {result['case_folding'][:12]}")
            print(f"[5] Lemmatization_result:   {result['lemmatization'][:12]}")
            print(f"[6] Stemming_result:    {result['stemming'][:12]}")
            print("." * 60)
            count += 1

    if os.path.exists(documents_path):
        display_results("DOCUMENTS", loader.load_documents(documents_path), limit=3)

    if os.path.exists(training_path):
        tweets_train = loader.load_tweets(training_path)
        display_results("TRAINING TWEETS", tweets_train, limit=5)

    if os.path.exists(validation_path):
        tweets_val = loader.load_tweets(validation_path)
        display_results("VALIDATION TWEETS", tweets_val, limit=5)
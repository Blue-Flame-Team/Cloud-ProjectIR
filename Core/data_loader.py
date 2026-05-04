import os
import csv


class DataLoader:

    def load_documents(self, folder_path: str) -> dict:
        documents = {}

        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)

                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                doc_name = filename.replace(".txt", "")
                documents[doc_name] = content

        return documents

    def load_tweets(self, csv_path: str) -> dict:
        tweets = {}
        tweet_id = 0

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 4:
                    text = row[3]
                    tweets[f"tweet_{tweet_id}"] = text
                    tweet_id += 1

        return tweets


if __name__ == "__main__":
    loader = DataLoader()

    docs = loader.load_documents("Data")
    print(f" Number of documents: {len(docs)}")
    for name, text in docs.items():
        print(f"{name}: {text[:60]}...")

    print("=" * 40)

    tweets = loader.load_tweets("Data/twitter_validation.csv")
    print(f" Number of tweets: {len(tweets)}")
    for name, text in list(tweets.items())[:5]:
        print(f"{name}: {text[:60]}...")


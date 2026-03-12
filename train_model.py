import json, pickle
from sklearn.feature_extraction.text import TfidfVectorizer

with open("data/syllabus_faq.json") as f:
    data = json.load(f)

questions = list(data.keys())
answers = list(data.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

with open("model.pkl", "wb") as f:
    pickle.dump((X, questions, answers, vectorizer), f)

print("Model trained and saved.")

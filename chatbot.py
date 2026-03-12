import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open("model.pkl", "rb") as f:
    X, questions, answers, vectorizer = pickle.load(f)

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    vec = vectorizer.transform([query])
    sim = cosine_similarity(vec, X)
    idx = sim.argmax()
    print("Bot:", answers[idx] if sim[0][idx] > 0.3 else "Sorry, I didn't get that.")

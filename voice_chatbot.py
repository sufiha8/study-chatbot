

import speech_recognition as sr, pyttsx3, pickle
from sklearn.metrics.pairwise import cosine_similarity

with open("model.pkl", "rb") as f:
    X, questions, answers, vectorizer = pickle.load(f)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(msg): print("Bot:", msg); engine.say(msg); engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except: return ""

speak("Ask your question.")
while True:
    query = listen()
    if not query or query.lower() in ["exit", "quit"]: break
    vec = vectorizer.transform([query])
    sim = cosine_similarity(vec, X)
    idx = sim.argmax()
    speak(answers[idx] if sim[0][idx] > 0.3 else "Sorry, I didn't understand.")

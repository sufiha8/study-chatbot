import tkinter as tk
import pickle
import pyttsx3
import speech_recognition as sr
from sklearn.metrics.pairwise import cosine_similarity

# Load model
with open("model.pkl", "rb") as f:
    X, questions, answers, vectorizer = pickle.load(f)

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            status.set("Listening...")
            root.update()
            audio = r.listen(source, timeout=5)
            query = r.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, query)
            ask_question()
        except:
            status.set("Could not understand. Try again.")
            speak("Sorry, I couldn't understand.")
            root.update()

def ask_question():
    query = entry.get()
    if not query.strip():
        status.set("Please enter a question.")
        return

    query_vec = vectorizer.transform([query])
    sim = cosine_similarity(query_vec, X)
    idx = sim.argmax()

    if sim[0][idx] < 0.3:
        response = "Sorry, I didn't understand that. Please try again."
    else:
        response = answers[idx]

    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, response)
    speak(response)
    status.set("Answered.")

# GUI
root = tk.Tk()
root.title("Study Voice Chatbot")
root.geometry("500x400")

tk.Label(root, text="Ask your syllabus-related question:").pack(pady=5)
entry = tk.Entry(root, width=60)
entry.pack(pady=10)

tk.Button(root, text="Ask", command=ask_question).pack(pady=5)
tk.Button(root, text="🎤 Speak", command=listen).pack(pady=5)

response_box = tk.Text(root, height=8, width=60)
response_box.pack(pady=10)

status = tk.StringVar()
status.set("Ready")
tk.Label(root, textvariable=status).pack(pady=5)

root.mainloop()

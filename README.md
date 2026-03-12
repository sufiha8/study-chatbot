# 📚 Study Chatbot (Python)

A beginner-friendly **terminal-based Study Chatbot** built using Python.
The chatbot allows students to ask **syllabus-related questions** and receive answers directly in the terminal.

This project supports **both text-based interaction and voice-based interaction**, where students can ask questions using their **microphone** and receive responses in **voice output**.

The chatbot currently uses **rule-based responses (hardcoded questions and answers)** designed for educational topics.


# 🚀 Features

* Terminal-based chatbot interface
* Beginner-friendly Python implementation
* Students can ask syllabus-related questions
* **Voice input support** (ask questions through microphone)
* **Voice output support** (chatbot replies using speech)
* Hardcoded question–answer responses
* Continuous conversation loop until user exits
* Lightweight and easy to run


# 🧠 How the Chatbot Works

The chatbot follows a **rule-based logic system**:

1. The user asks a question either by **typing** or **speaking through the microphone**.
2. The chatbot processes the input.
3. The program checks the question using **Python conditional statements**.
4. If the question matches predefined keywords, the chatbot returns the stored answer.
5. The chatbot then **speaks the answer using text-to-speech**.
6. If the question does not match any stored topic, the chatbot returns a default response.


# 🎤 Voice Interaction

The chatbot supports **voice interaction**, allowing a more natural way for students to ask questions.

### Voice Input

Students can ask questions using the **microphone**. The chatbot converts speech into text using **speech recognition**.

### Voice Output

The chatbot responds by converting text answers into **speech output**, allowing the response to be heard instead of only displayed.

# 💻 Technologies Used

* Python
* Speech Recognition
* Text-to-Speech
* Command Line Interface (CLI)

Libraries used:

* `speechrecognition` – converts voice to text
* `pyttsx3` – converts text to voice

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

git clone https://github.com/sufiha8/study-chatbot.git

## 2️⃣ Navigate to the Project Folder

cd study-chatbot

## 3️⃣ Install Dependencies

pip install speechrecognition
pip install pyttsx3
pip install pyaudio

*(pyaudio is required for microphone input)*

## ▶️ Run the Chatbot

python chatbot.py

# 💬 Example Interaction

### Text Mode

📚 Study Chatbot Started!

You: hello
Chatbot: Hello! How can I help you with your studies?

### Voice Mode

Student speaks through microphone:

"What is Python?"

Chatbot responds with voice:

"Python is a popular programming language used for AI, web development, and automation."

# 🎯 Learning Objectives

This project helps beginners understand:

* Basic chatbot design
* Python loops and conditional statements
* Speech recognition integration
* Text-to-speech systems
* Command-line interaction
* Building simple educational AI tools

# 📌 Use Case

This chatbot can act as a **basic educational assistant** where:

* Students ask questions related to their syllabus
* The chatbot provides quick answers
* Voice interaction improves accessibility and usability

# 🔮 Future Improvements

This project is planned to evolve into a **full AI-powered educational platform**.

Future features include:

* Convert chatbot into a **mobile application**
* Teacher dashboard for **chapter-wise questions and answers**
* Subject-wise knowledge database
* **AI-based doubt solving chatbot**
* Student authentication system
* Chat history tracking
* Voice-based study assistant
* Integration with **AI APIs for advanced responses**

# 🏗 Future System Architecture

Student App / Web Interface
            │
            ▼
        AI Chatbot
            │
            ▼
     Subject Knowledge Base
            │
            ▼
      Teacher Dashboard
 (Upload chapter-wise Q&A)



# 👩‍💻 Author

Developed by Sufiha Khan

# ⭐ Support

If you found this project useful, consider **starring the repository on GitHub** ⭐

Contributions and suggestions are welcome.

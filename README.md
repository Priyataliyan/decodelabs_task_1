# 🤖 Rule-Based AI Chatbot

A beginner-friendly **Rule-Based AI Chatbot built with Python**.  
The chatbot responds to predefined user inputs using `if-elif-else` decision-making logic and runs continuously until the user exits.

## 📌 Project Overview

This project demonstrates the basic principles of a rule-based artificial intelligence system. Instead of machine learning, the chatbot uses explicitly defined rules to determine an appropriate response.

The project focuses on:

- Control flow
- Decision-making logic
- User input processing
- Conditional statements
- Continuous interaction using loops
- Basic AI concepts

## ✨ Features

- Responds to greetings such as `hello`, `hi`, and `hey`
- Answers basic questions
- Tells the user its name
- Explains what it can do
- Provides a simple explanation of Artificial Intelligence
- Responds to thanks
- Handles unknown inputs with a default response
- Supports exit commands: `bye`, `exit`, and `quit`
- Runs in a continuous conversation loop

## 🛠️ Technologies Used

- **Python 3**
- Python `input()`
- `if-elif-else`
- `while` loop
- Functions
- String methods such as `.lower()` and `.strip()`

## 📂 Project Structure

```text
Rule-Based-AI-Chatbot/
│
├── chatbot.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Rule-Based-AI-Chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

If `python` does not work on Windows, try:

```bash
py chatbot.py
```

## 💬 Example Conversation

```text
=============================================
       🤖 Welcome to PyBot 🤖
=============================================
Type 'bye', 'exit', or 'quit' to stop.

You: hello
Bot: Hello! Welcome to my AI Chatbot.

You: what is your name
Bot: My name is PyBot.

You: what can you do
Bot: I can answer basic questions using predefined rules.

You: what is ai
Bot: Artificial Intelligence is the simulation of human intelligence in machines.

You: thanks
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a great day.
```

## 🧠 How It Works

The chatbot receives text from the user and first normalizes it:

```python
user_input = user_input.lower().strip()
```

It then checks the input against predefined rules:

```python
if user_input in ["hello", "hi", "hey"]:
    return "Hello! Welcome to my AI Chatbot."
```

If no rule matches, the chatbot uses a default response.

The conversation continues inside a `while` loop until the user enters an exit command.

## 🎯 Learning Objectives

This project helps demonstrate:

1. Python functions
2. Conditional statements
3. Loops
4. String processing
5. Basic decision-making systems
6. Fundamental rule-based AI concepts
7. Human-computer interaction through a command-line interface

## ⚠️ Limitations

This chatbot does not learn from conversations or understand natural language like a modern large language model. It can only respond to inputs covered by its predefined rules.

## 🔮 Future Improvements

Possible improvements include:

- Add more conversation rules
- Add more question categories
- Add a graphical user interface using Tkinter
- Add voice input and output
- Add natural language processing
- Store conversation history
- Connect the chatbot to a database
- Add machine-learning capabilities

## 👩‍💻 Author

**Priya Taliyan**

### Project

**Rule-Based AI Chatbot**

### Language

**Python**

---

⭐ If you find this project useful, consider giving the repository a star!

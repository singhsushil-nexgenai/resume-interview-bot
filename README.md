# 🤖 Resume Interview Prep Bot

An AI-powered chatbot that reads my resume and answers interview questions in first person — built with OpenAI API and Gradio.

---

## 🎯 What it Does

- 📄 Reads a PDF resume automatically
- 🧠 Roleplays as the candidate in a real interview
- 💬 Answers questions based **only** on resume content
- 🔁 Remembers previous questions in the conversation (memory)
- 🖥️ Clean chat UI powered by Gradio

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenAI API (gpt-4o-mini) | AI brain powering the chatbot |
| Gradio | Interactive chat UI |
| pypdf | Extracts text from PDF resume |
| python-dotenv | Manages API key securely |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/singhsushil-nexgenai/resume-interview-bot.git
cd resume-interview-bot
```

### 2. Install dependencies
```bash
pip install openai gradio pypdf python-dotenv
```

### 3. Add your API key
Create a `.env` file in the project folder:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 4. Add your resume
Place your resume as `resume.pdf` in the project folder.

### 5. Run the app
```bash
python app.py
```
Open `http://127.0.0.1:7860` in your browser.

---

## 💬 Example Questions to Ask

- *"Tell me about yourself."*
- *"What are your strongest technical skills?"*
- *"Describe a challenging project you worked on."*
- *"What is your educational background?"*
- *"Why should we hire you?"*

---

## 🧠 How It Works

```
User asks a question
        ↓
Gradio UI captures the message
        ↓
System prompt (resume injected) + conversation history sent to OpenAI
        ↓
GPT-4o-mini generates answer as the candidate
        ↓
Answer displayed in chat UI
        ↓
History updated for next question (memory)
```

---

## 📁 Project Structure

```
resume-interview-bot/
├── app.py                          # Main Gradio app
├── resume_interview_prep_bot.ipynb # Jupyter notebook (assignment)
├── requirements.txt                # Python dependencies
├── resume.pdf                      # Resume (PDF)
└── README.md                       # This file
```

---

## 👨‍💻 Author

**Sushil Kumar Singh**
- 📧 singhsushil.nexgenai@gmail.com
- 🐙 [github.com/singhsushil-nexgenai](https://github.com/singhsushil-nexgenai)

---

## 📚 Built As Part Of
**GenAI Bootcamp — Week 1 Assignment**

import os
import pypdf
import gradio as gr
from openai import OpenAI

# ── OpenAI client ──────────────────────────────────────────────
# API key is stored as a Secret in Hugging Face Space settings
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── Load resume from PDF ───────────────────────────────────────
def load_resume(path="resume.pdf"):
    if not os.path.exists(path):
        return ""
    reader = pypdf.PdfReader(path)
    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)
    return "\n".join(pages_text).strip()

resume_text = load_resume()

# ── System prompt ──────────────────────────────────────────────
system_prompt = f"""You are roleplaying as the job candidate described in the resume below.

Your role is to answer interview questions in the first person, exactly as the candidate would in a real job interview.

Rules you must follow:
1. Always speak in first person ("I", "my", "me", "we" when referring to team work)
2. Only use facts, skills, and experiences that appear in the resume — never invent or guess
3. Be concise, confident, and professional — give focused answers like a real interview
4. If a question cannot be answered from the resume, respond with:
   "That's not something I've covered in my resume, but I'd be happy to discuss it in more detail."
5. Do not break character or refer to "the resume" as a document in your answers
6. Do not answer questions completely unrelated to the interview (e.g. geography trivia)

--- RESUME START ---
{resume_text}
--- RESUME END ---
"""

# ── Chatbot function ───────────────────────────────────────────
def interview_bot(message, history):
    messages = [{"role": "system", "content": system_prompt}]
    for item in history:
        messages.append({"role": item["role"], "content": item["content"]})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# ── Gradio UI ──────────────────────────────────────────────────
demo = gr.ChatInterface(
    fn=interview_bot,
    title="🤖 Resume Interview Prep Bot",
    description=(
        "Ask me any interview question and I'll answer as the candidate — "
        "based only on what's in my resume."
    ),
    examples=[
        "Tell me about yourself.",
        "What are your strongest technical skills?",
        "Describe a challenging project you worked on.",
        "What is your educational background?",
        "Why should we hire you?"
    ]
)

demo.launch()

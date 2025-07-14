import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo")

def analyze_resume(resume: str, job: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        """
You are an HR expert assistant.
Compare the following resume and job description.
Give:
1. A match percentage (0–100%)
2. 2–3 strengths in resume
3. 2–3 missing skills
4. How to improve resume to match job better

Resume:
{resume}

Job Description:
{job}
"""
    )
    messages = prompt.format_messages(resume=resume, job=job)
    response = llm(messages)
    return response.content
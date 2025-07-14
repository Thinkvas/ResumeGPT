# 📄 ResumeGPT – AI-Powered Resume Matcher

**ResumeGPT** is a smart LLM-powered app that compares your resume with any job description and gives instant feedback — including match score, strengths, missing skills, and improvement suggestions.

Built with **LangChain**, **OpenAI GPT-3.5**, and **Streamlit**.

---

## 🚀 Features

✅ Match your resume to any job description  
✅ Get a match percentage score (0–100%)  
✅ Identify strong points in your resume  
✅ See missing skills or keywords  
✅ Get improvement tips from an AI assistant



---

## 📥 Sample Input / Output

**Resume**
```
Srinivas Siripella  
B.Tech in AI & ML  
Skills: Python, LangChain, Streamlit, Git, LLMs  
```

**Job Description**
```
Looking for an AI/ML intern with experience in Python, LLMs, LangChain, Git, and Streamlit. Must understand prompt engineering and API integration.
```

**🧠 AI Output**
- 🔢 Match Score: 88%  
- ✅ Strengths: Python, LangChain, Streamlit  
- ⚠️ Missing: API integration, prompt engineering  
- 🛠 Suggestions: Add a project using APIs, mention prompt skills in resume

---

## ⚙️ Installation

```bash
git clone https://github.com/Thinkvas/ResumeGPT.git
cd ResumeGPT
pip install -r requirements.txt
```

> Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your-openai-key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
ResumeGPT/
├── app.py
├── utils.py
├── .env            # add this manually; excluded from GitHub
├── requirements.txt
├── .gitignore
├── sample_resume.txt
├── sample_job.txt
└── README.md
```

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- Python 3.10+

---

## 💼 Author

**Srinivas Siripella**  
🔗 [GitHub](https://github.com/Thinkvas)

---

## 🛡 License

This project is licensed under the MIT License.

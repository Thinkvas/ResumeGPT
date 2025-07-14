import streamlit as st
from utils import analyze_resume
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="ResumeGPT", page_icon="📄")

st.title("📄 ResumeGPT - Resume vs JD Analyzer")

resume_text = st.text_area("Paste your Resume text here:", height=200)
job_desc = st.text_area("Paste Job Description here:", height=200)

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        result = analyze_resume(resume_text, job_desc)
        st.subheader("✅ Match Report")
        st.markdown(result)
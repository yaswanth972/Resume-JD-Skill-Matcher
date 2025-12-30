# app.py
"""Streamlit web application for Resume-JD Skill Matching."""
import streamlit as st
from src.matcher import match_resume_jd

st.set_page_config(
    page_title="Resume–JD Skill Matcher",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Resume–Job Description Skill Matcher")
st.write(
    "This tool uses **NLP & sentence embeddings** to calculate how well a resume matches a job description."
)

resume_text = st.text_area("📌 Paste Resume Text", height=200)
jd_text = st.text_area("📌 Paste Job Description", height=200)

if st.button("🔍 Match Skills"):
    if resume_text.strip() == "" or jd_text.strip() == "":
        st.warning("Please paste both Resume and Job Description.")
    else:
        try:
            score = match_resume_jd(resume_text, jd_text)

            st.success(f"✅ Skill Match Score: **{score}%**")

            if score >= 75:
                st.info("🔥 Strong match! Resume aligns well with the job.")
            elif score >= 50:
                st.warning("⚠️ Moderate match. Consider improving some skills.")
            else:
                st.error("❌ Low match. Resume needs significant updates.")
        except Exception as e:
            st.error(f"Error processing texts: {str(e)}")

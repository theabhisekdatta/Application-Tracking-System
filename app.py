import streamlit as st
import PyPDF2 as pdf
from utilities.text_matching import calculate_similarity
from utilities.missing_keywords import find_missing_keywords
from utilities.extract_summary import generate_summary


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# streamlit app
st.title(":blue[Application Tracking System]")
st.text("Check your resume")

# Job Description Loading..
jd = st.text_area("Paste the Job Description")


uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please uplaod the pdf")

submit = st.button("Check your Resume")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        jd_matching = calculate_similarity(jd, text)
        missing_keywords = find_missing_keywords(text, jd)
        summary = generate_summary(jd)
        st.write("Job Description Matching: ", f"{jd_matching:.2f}%")
        st.text_area("Summary", value=summary, height=200)

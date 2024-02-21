import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from utilities.text_matching import calculate_similarity
from utilities.missing_keywords import find_missing_keywords
from utilities.extract_summary import generate_summary

load_dotenv()  # load all our environment variables


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# # Load pre-trained Word2Vec model
# model_file_path = "pretrain_word2vec-google-news-300"
# with open(model_file_path, 'rb') as f:
#     word2vec_model = pickle.load(f)


def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template


input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"MissingKeywords:[]","Job Description Summary":""}}
"""

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
        response = get_gemini_repsonse(input_prompt)
        st.write("Job Description Matching: ", f"{jd_matching:.2f}%")
        st.write("Job Description Summary: ", summary)
        st.write("Missing Keywords from the Resume: ", missing_keywords)
        # st.write(response)

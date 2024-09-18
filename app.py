# Set up the Local Environment
from dotenv import load_dotenv
load_dotenv() # setup local environment
import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile


# Lets setup streamlit front end and read the pdf document
#st.set_page_config("Career Compass")

st.header("🎯Career Compass: :blue[Your AI-Powered Resume Navigator] 👩🏻‍💻📓✍🏻💡", divider = "green")
st.subheader("🔰 Tips for Using this Application: ")
notes = f'''
* **Upload Your Resume (PDF):** The first step on your journey to career success. Let's analyze your skills and experience.
* **Paste the Target Job Description:** Share the details of your dream job, and we'll help you bridge the gap.
* **Unleash the Power of AI:** Watch as our AI-powered engine analyzes your resume against the job description, providing personalized insights and recommendations to boost your chances of success.'''
st.write(notes)

st.sidebar.subheader(body="Upload your Resume📌")
pdf_doc = st.sidebar.file_uploader("Please upload the pdf here 🔰: ",type =['pdf'])

st.subheader("Enter the Job Description 📋", divider = True)
job_desc= st.text_area(label = "Copy Paste the Job Description from Linked-In or any other Portal", 
                        max_chars=10000)

submit = st.button(label="🔰 Get AI-Powered Insight 🔐")
if submit:
    st.markdown(profile(pdf_doc=pdf_doc, job_desc=job_desc))
    


st.subheader("Disclaimer: ", divider = True)
notes = f'''
1. The ATS score and probability of success are estimates and should be used as guidance, not definitive predictions.
2. The AI-generated suggestions and resume narrative are meant to assist you, but always review and tailor them to your situation.'''
st.write(notes)

st.footer("created by Mukul Chauhan")











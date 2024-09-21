import streamlit as st
import google.generativeai as genai
from pdf import read_pdf

import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-1.5-flash") # Initiate Model

# Read the PDF and store it into pdf_doc.
def profile(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf = read_pdf(pdf_doc)
        st.sidebar.markdown("The Resume has been Uploaded ✅️ 👍") 
    else:
        st.warning("👈 Upload your Resume")
    ats_score = model.generate_content(f"Compare the resume '{pdf}' with the job description '{job_desc}' & suggest the ATS Score(in pecentage) of the resume. ")
    probability = model.generate_content(f"Compare the resume '{pdf}' with the job description '{job_desc}' & suggest the Probability(in pecentage) of Getting Selected. ")
    keyword_analysis = model.generate_content(f"Analyze keywords missing in the resume '{pdf}' compared to the job description and mention them in bold '{job_desc}'")
    swot_analysis = model.generate_content(f"Provide a SWOT analysis of the resume '{pdf}' in the context of the job description '{job_desc}'")
    improvement_tips = model.generate_content(f"Suggest improvements to the resume '{pdf}' to better align with the job description and mention the comments in bold  '{job_desc}'")
    resume_narrative = model.generate_content(f"Rewrite the resume '{pdf}' to highlight relevant skills and experience accordng to the job description '{job_desc}'")
        
    # Display Results
    return{#st.subheader(body = "Resume ATS Score"),
           st.write(ats_score.text),
           #st.subheader(body = "Probability of Getting Selected"),
           st.write(probability.text),
           #st.subheader("Keyword Analysis"),
           st.write(keyword_analysis.text),
           #st.subheader("SWOT Analysis"),
           st.write(swot_analysis.text),
           #st.subheader("Improvement Tips"),
           st.write(improvement_tips.text),
           #st.subheader("Enhanced Resume Narrative"),
           st.write(resume_narrative.text)}    
    
    
    
    
    

import streamlit as st
import google.generativeai as genai
from pdf import read_pdf
from docx import read_docx

import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel("gemini-1.5-flash") # Initiate Model

# Read the PDF or DOCX and store it into doc.
def profile(doc, job_desc):
    if doc is not None:
        if doc.name.endswith('.pdf'):
            content = read_pdf(doc)
            st.sidebar.markdown("The PDF Resume has been Uploaded ✅️ 👍")
        elif doc.name.endswith('.docx'):
            content = read_docx(doc)
            st.sidebar.markdown("The DOCX Resume has been Uploaded ✅️ 👍")
        else:
            st.warning("Unsupported file type. Please upload a PDF or DOCX file.")
            return
    else:
        st.warning("👈 Upload your Resume")
        return

    ats_score = model.generate_content(f"Compare the resume '{content}' with the job description '{job_desc}' & suggest the ATS Score(in percentage) of the resume.")
    probability = model.generate_content(f"Compare the resume '{content}' with the job description '{job_desc}' & suggest the Probability(in percentage) of Getting Selected.")
    keyword_analysis = model.generate_content(f"Analyze keywords missing in the resume '{content}' compared to the job description and mention them in bold '{job_desc}'")
    swot_analysis = model.generate_content(f"Provide a SWOT analysis of the resume '{content}' in the context of the job description '{job_desc}'")
    improvement_tips = model.generate_content(f"Suggest improvements to the resume '{content}' to better align with the job description and mention the comments in bold '{job_desc}'")
    resume_narrative = model.generate_content(f"Rewrite the resume '{content}' to highlight relevant skills and experience according to the job description '{job_desc}'")
        
    # Display Results
    return {
        st.write(ats_score.text),
        st.write(probability.text),
        st.write(keyword_analysis.text),
        st.write(swot_analysis.text),
        st.write(improvement_tips.text),
        st.write(resume_narrative.text)
    }
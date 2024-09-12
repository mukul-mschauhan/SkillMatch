# Career Compass: Your AI-Powered Resume Navigator

![WhatsApp Image 2024-09-12 at 10 47 13](https://github.com/user-attachments/assets/345460ab-34aa-480e-b7fe-3cee34144478)


**Empower your job search with AI-driven resume analysis and optimization.** 

Career Compass is a Streamlit application that helps you tailor your resume to specific job descriptions, increasing your chances of success.  Leveraging the power of Large Language Models (LLMs) and natural language processing (NLP), it provides insights into your resume's strengths and weaknesses, identifies missing keywords, and offers actionable tips for improvement. 

## Features

* **ATS Score:** Get an estimated Applicant Tracking System (ATS) score to gauge your resume's compatibility with automated screening tools.
* **Probability of Success:** Receive an estimated probability of success based on your resume's alignment with the job description.
* **Keyword Analysis:** Identify keywords missing from your resume compared to the target job description.
* **SWOT Analysis:** Get a comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis of your resume in the job context.
* **Improvement Tips:** Receive personalized suggestions on enhancing your resume's content and structure.
* **Resume Narrative:** Get an AI-generated rewrite of your resume, highlighting relevant skills and experience for the target job.

## How to Use

1. **Upload your resume in PDF format.**
2. **Paste the job description you're targeting.**
3. **Click "Analyze & Optimize" and let the AI work its magic!**

## Technical Stack

* **Streamlit:** For building the interactive web application.
* **Python-dotenv:** For managing environment variables (e.g., OpenAI API key).
* **Google GenerativeAI:** For leveraging large language models for analysis and generation.
* **PyPDF2:** For extracting text from PDF resumes.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/Career-Compass.git`
2. Navigate to the project directory: `cd Career-Compass`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
    * On Windows: `.venv\Scripts\activate`
    * On macOS/Linux:   
 `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`   

6. Set up your OpenAI API key in a `.env` file.
7. Run the app: `streamlit run app.py`

## Disclaimer

* The ATS score and probability of success are estimates and should be used as guidance, not definitive predictions.
* The AI-generated suggestions and resume narrative are meant to assist you, but always review and tailor them to your situation.

**Happy job hunting!**

from pypdf import PdfReader
import streamlit as st
from typing_extensions import Concatenate


def read_pdf(pdf_doc):
    pdf = PdfReader(pdf_doc)
    # Saving the entire pdf as a raw_text
    raw_text = ' '
    for i, page in enumerate(pdf.pages):
        content = page.extract_text()
        if content:
            raw_text +=content
    return(raw_text)



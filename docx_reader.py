import docx
import io
from PIL import Image
import pytesseract

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image = Image.open(io.BytesIO(rel.target_part.blob))
            text += pytesseract.image_to_string(image)
    return text
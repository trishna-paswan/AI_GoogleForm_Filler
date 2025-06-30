# extract_data.py 

import fitz  # PyMuPDF
import spacy
import re

nlp = spacy.load("en_core_web_sm")
 
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_info(text):
    doc = nlp(text)
    data = {
        "Name": None,
        "Email": None,
        "Phone": None,
        "DOB": None,
        "Address": None
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not data["Name"]:
            data["Name"] = ent.text
        elif ent.label_ == "GPE" and not data["Address"]:
            data["Address"] = ent.text

    email_match = re.search(r"\b[\w.-]+?@\w+?\.\w+?\b", text)
    phone_match = re.search(r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b", text)
    dob_match = re.search(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)

    if email_match:
        data["Email"] = email_match.group()
    if phone_match:
        data["Phone"] = phone_match.group()
    if dob_match:
        data["DOB"] = dob_match.group()

    return data

def get_personal_data_from_pdf(file_path):
    text = extract_text_from_pdf(file_path)
    return extract_info(text)

import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_phone(text):

    pattern = r"(\+?\d[\d\s\-]{8,}\d)"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":

            return ent.text

    return ""


def extract_candidate_details(text):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text)
    }
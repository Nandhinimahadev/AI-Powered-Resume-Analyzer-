import spacy
import json

nlp = spacy.load("en_core_web_sm")

with open("model/skills.json", "r") as f:
    SKILLS = set(json.load(f))


def extract_entities(text):
    doc = nlp(text)
    entities = {"Names": [], "Emails": [], "Phones": [], "Skills": []}

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["Names"].append(ent.text)
        elif ent.label_ == "EMAIL":
            entities["Emails"].append(ent.text)
        elif ent.label_ == "PHONE":
            entities["Phones"].append(ent.text)
    words = set(word.lower() for word in text.split())
    entities["Skills"] = list(words.intersection(SKILLS))

    return entities

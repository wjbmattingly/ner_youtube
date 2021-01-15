#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 09.06             #
#   Building Holocaust NER Pipeline   #
#        Training the New Model       #
#               with                  #
#        Dr. W.J.B. Mattingly         #
import spacy
from spacy.tokens import Span

main_nlp = spacy.blank("en")

english_nlp = spacy.load("en_core_web_sm")
english_ner = english_nlp.get_pipe("ner")
main_nlp.add_pipe(english_ner, name="en_dln")

def en_narrow(doc):
    labels = ["DATE", "GPE", "NORP"]
    l = []
    for old_ent in doc.ents:
        if old_ent.label_ == "DATE":
            l.append(old_ent)
        elif old_ent.label_ == "GPE":
            new_ent = Span(doc, old_ent.start, old_ent.end, label="LOCATION")
            l.append(new_ent)
        elif old_ent.label_ == "NORP":
            l.append(old_ent)
    l = tuple(l)
    print (doc.ents)
    doc.ents = l
    print (doc.ents)
    return (doc)

main_nlp.add_pipe(en_narrow, name="en_narrow", after="en_dln")




###PERSON --- END OF PIPELINE
person_nlp = spacy.load("en_core_web_sm")
person_ner = person_nlp.get_pipe("ner")
main_nlp.add_pipe(person_ner, "person_en_ner")

def person_narrow(doc):
    labels = ["PERSON"]
    previous_labels = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP"]
    l = []
    for old_ent in doc.ents:
        if old_ent.label_ == "PERSON":
            l.append(old_ent)
        elif old_ent.label_ in previous_labels:
            l.append(old_ent)
    l = tuple(l)
    doc.ents = l
    return (doc)

main_nlp.add_pipe(person_narrow, name="person_narrow", after="person_en_ner")

text = "In 1942, WWII took place. Treblinka is a location in modern-day Poland. Meir Bornstein is a person."
doc = main_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)

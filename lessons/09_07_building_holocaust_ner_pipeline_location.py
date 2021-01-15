#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 09.07             #
#   Building Holocaust NER Pipeline   #
#        Training the New Model       #
#               with                  #
#        Dr. W.J.B. Mattingly         #
import spacy
from spacy.tokens import Span

#MAIN NLP OBJECT
main_nlp = spacy.blank("en")
new_vocab = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP", "EVENT", "GPE", "PERSON" "CARDINAL", "FAC", "LANGUAGE", "LAW", "LOC", "MONEY", "ORDINAL", "ORG", "PERCENT", "PRODUCT", "QUANTITY", "TIME", "WORK_OF_ART"]
for item in new_vocab:
    main_nlp.vocab.strings.add(item)


####GET CAMPS####
camp_nlp = spacy.load("./pretrained_models/camp_ner")
camp_ner = camp_nlp.get_pipe("ner")
main_nlp.add_pipe(camp_ner, name="camp_ner")


###GET GHETTOS########
ghetto_nlp = spacy.load("./pretrained_models/ghetto_ner")
ghetto_ner = ghetto_nlp.get_pipe("ner")
main_nlp.add_pipe(ghetto_ner, name="ghetto_ner")


###GET EVENTS####
event_nlp = spacy.load("./pretrained_models/events_ner")
event_ner = event_nlp.get_pipe("ner")
main_nlp.add_pipe(event_ner, name="event_ner")


###GET EASTERN-EUROPEAN LOCS######
eastern_europe_nlp = spacy.load("./pretrained_models/eastern_europe_ner_good")
eastern_europe_ner = eastern_europe_nlp.get_pipe("ner")
main_nlp.add_pipe(eastern_europe_ner, name="eastern_europe_ner")


# ###GET DATES, GPE, AND NORPS
english_nlp = spacy.load("en_core_web_sm")
english_ner = english_nlp.get_pipe("ner")
main_nlp.add_pipe(english_ner, name="en_dln")

def en_narrow(doc):
    labels = ["DATE", "GPE", "NORP"]
    previous_labels = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP", "EVENT"]
    l = []
    for old_ent in doc.ents:
        if old_ent.label_ == "DATE":
            l.append(old_ent)
        elif old_ent.label_ == "GPE":
            new_ent = Span(doc, old_ent.start, old_ent.end, label="LOCATION")
            l.append(new_ent)
        elif old_ent.label_ == "NORP":
            l.append(old_ent)
        elif old_ent.label_ in previous_labels:
            l.append(old_ent)
    l = tuple(l)
    doc.ents = l
    return (doc)

main_nlp.add_pipe(en_narrow, name="en_narrow", after="en_dln")



###PERSON --- END OF PIPELINE
person_nlp = spacy.load("en_core_web_sm")
person_ner = person_nlp.get_pipe("ner")
main_nlp.add_pipe(person_ner, "person_en_ner")

def person_narrow(doc):
    labels = ["PERSON"]
    previous_labels = ["CAMP", "GHETTO", "DATE", "LOCATION", "NORP", "EVENT"]
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


with open ("data/test.txt", "r", encoding="utf-8") as f:
    text = f.read()
doc = main_nlp(text)
all_labels = []
all_ents = []
for ent in doc.ents:
    all_labels.append(ent.label_)
    all_ents.append(ent.text)

all_labels = list(set(all_labels))
all_ents = list(set(all_ents))
with open("data/results.txt", "w", encoding="utf-8") as f:
    f.write (f"Total Entities found: {len(doc.ents)}\n")
    f.write (f"{len(all_labels)} Unique Labels found: {str(all_labels)}\n")
    f.write (f"{len(all_ents)} Unique Entities found: {str(all_ents)}\n")
    for ent in doc.ents:
        f.write (f"{ent.text}, {ent.label_}")
        f.write("\n")

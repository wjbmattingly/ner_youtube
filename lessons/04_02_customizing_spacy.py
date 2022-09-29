#   NAMED ENTITY RECOGNITION SERIES   #
#             Lesson 04.02            #
#        Leveraging spaCy's NER       #
#               with                  #
#        Dr. W.J.B. Mattingly         #
import spacy
import json
import random

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def test_model(model, text):
    doc = nlp(text)
    results = []
    entities = []
    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char, ent.label_))
    if len(entities) > 0:
        results = [text, {"entities": entities}]
        return (results)

#TRAIN_DATA = [(text, {"entities": [(start, end, label)]})]

nlp = spacy.load("hp_ner")
TRAIN_DATA = []
with open ("data/hp.txt", "r")as f:
    text = f.read()

    chapters = text.split("CHAPTER")[1:]
    for chapter in chapters:
        chapter_num, chapter_title = chapter.split("\n\n")[0:2]
        chapter_num = chapter_num.strip()
        segments = chapter.split("\n\n")[2:]
        for segment in segments:
            segment = segment.strip()
            segment = segment.replace("\n", " ")
            results = test_model(nlp, segment)
            if results != None:
                TRAIN_DATA.append(results)

print (len(TRAIN_DATA))
# save_data("data/hp_training_data.json", TRAIN_DATA)

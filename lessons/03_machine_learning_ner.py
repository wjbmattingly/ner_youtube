#   NAMED ENTITY RECOGNITION SERIES   #
#             Lesson 03               #
#        Machine Learning NER         #
#               with                  #
#        Dr. W.J.B. Mattingly         #
import spacy

test = "Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere."

nlp = spacy.load("en_core_web_lg")
doc = nlp(test)
for ent in doc.ents:
    print (ent.text, ent.label_)

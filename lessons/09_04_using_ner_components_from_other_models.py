#   NAMED ENTITY RECOGNITION SERIES   #
#            Lesson 09.04             #
# Adding Pipes Old Pipes to New Models#
#        Training the New Model       #
#               with                  #
#        Dr. W.J.B. Mattingly         #
import spacy

new_vocab = ["CONC_CAMP"]
main_nlp = spacy.load("en_core_web_sm")

for item in new_vocab:
    main_nlp.vocab.strings.add(item)

conc_camps_nlp = spacy.load("conc_camps_model")
ner = conc_camps_nlp.get_pipe("ner")

main_nlp.add_pipe(ner, name="conc_camp_ner", before="ner")

main_nlp.to_disk("main_model")

doc = main_nlp("But you traveled from Lakhva to Lodz with your father. So, when the Germans came to Lakhva, did they form the ghetto immediately?  So, have nothing to do there, and they start the ghetto in Warsaw? And after they start to evacuate the ghetto, to take to Majdanek, to Treblinka, and the peoples they start to know they kill these people. This is the town of Plonsk. Warsaw is also a city in Poland. Pomiechowek is also a city in Poland. The Lakvha ghetto. USHMM Archive. United States Holocaust Memorial Museum. David A. Kochalski, born May 5, 1928 in Poland")
for ent in doc.ents:
    print (ent.text, ent.label_)

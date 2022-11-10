#   NAMED ENTITY RECOGNITION SERIES   #
#             Lesson 02               #
#          Rules-Based NER            #
#               with                  #
#        Dr. W.J.B. Mattingly         #

# Demonstrates the weakness of rule-based NER
# Requires programmer to write for whole bunch of code to do simple task

import json

with open("data/hp.txt", "r", encoding="utf-8") as f: #load text
    text = f.read().split("\n\n") #break up text by line break

character_names = []

with open("data/hp_characters.json", "r", encoding="UTF-8") as f: 
    characters = json.load(f) #load characters
    
    #iterate across all characters
    for character in characters:
        names = character.split()

        for name in names:
            if "and" != name and "the" != name and "The" != name:
                xname = name.replace(",", "").strip()
                character_names.append(name)

#break up text segment by segment
for segment in text:
    segment = segment.strip() #remove leading/trailing spaces in text
    segment = segment.replace("\n", " ") #remove line breaks
    print(segment)

    #get rid of punctuation marks
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    for ele in segment:
        if ele in punc:
            segment = segment.replace(ele, "")

    # need sentences split up into individual words
    words = segment.split() #split words based on white spaces

    i = 0
    for word in words: #check if word is a character
        if word in character_names:
            if words[i-1][0].isupper(): #check if capitalized (ex. "The Grinch")
                print(f"Found Character(s): {words[i-1]}{word}")
            else:
                print(f"Found Character(s): {word}")
        i = i+1
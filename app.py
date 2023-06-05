import spacy

nlp = spacy.load("en_core_web_lg")

file_path = "file.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

doc = nlp(text)

seen_entities = set()

for entity in doc.ents:
    if entity.text not in seen_entities:
        print(entity.text, entity.label_)
        seen_entities.add(entity.text)

# Load pre-existing spacy model
import spacy
import pickle
nlp = spacy.load('en_core_web_sm')
ner = nlp.get_pipe("ner")


test_data = []
train_data = []

tags = {'QUANTITY', 'TEMP', 'SIZE', 'NAME', 'STATE', 'UNIT', 'DF'}

with open("data/test.bin", "rb") as f:
    test_data = pickle.load(f)

with open("data/train.bin", "rb") as f:
    train_data = pickle.load(f)


for tag in tags:
    print(tag)
    ner.add_label(tag)

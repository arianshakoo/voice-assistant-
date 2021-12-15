import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import random 
import json

with open("intents.json") as file:
    data = json.laod(file)

words = []
labels = []
docs = []

for intent in data["intents"]:
    for pattern in intent["paterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

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
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["paterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)
        docs_x.append(pattern)
        docs_y.append(intent["tag"])
        if intent["tag"] not in labels:
            labels.append(intent["tag"])

word = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

labels = sorted(labels)

traning = []
output = []

out_empty = [0 for _ in range(len(classes))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row [classes.index(docs_y[x])] = 1

    traning.append(bag)
    output.append(output_row)

traning = numpy.array(traning)
output = np.array(output)
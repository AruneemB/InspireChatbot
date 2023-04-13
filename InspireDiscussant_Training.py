import random
import json
import pickle

import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

#Creates a lemmatizer which reduces each word down to its base, canonical dictionary form
#For example, the words change, changing, changes, changed, and changer would all be reduced to change through the lemmatizer
lemmatizer = WordNetLemmatizer()

#Reads the content from the json file in the form of text and loads it
#This loaded text is saved to the InspireDiscussant_Intents object and acts as a sort of dictionary Inspire can use to understand the user
InspireDiscussant_Intents = json.loads(open("InspireDiscussant_Intents.json").read())

words = []
classes = []
documents = []

ignoreCharacters = [".", ",", ";", ":", "?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/"]

for intent in InspireDiscussant_Intents["InspireIntents"]:
    for pattern in InspireDiscussant_Intents["intentPatterns"]:
        wordList = nltk.word_tokenize(pattern)
        words.append(wordList)
        documents.append((wordList, InspireDiscussant_Intents["intentTag"]))
        if InspireDiscussant_Intents["intentTag"] not in classes:
            classes.append(InspireDiscussant_Intents["intentTag"])

words = [lemmatizer.lemmatize(word) for word in words if ignoreCharacters not in word]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(words, open("classes.pkl", "wb"))

training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        if word in wordPatterns:
            bag.append(1)
        else:
            bag.append(0)

    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append([bag, outputRow])

    random.shuffle(training)
    training = np.array(training)

    trainX = list(training[:, 0])
    trainY = list(training[:, 1])

    model = Sequential()
    model.add(Dense(128, inputShape = (len(trainX[0])), activation = "relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation = "relu"))
    model.add(Drouput(0.5))
    model.add(Dense(len(trainingY[0]), activation = "softmax"))

    sgd = SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
    model.compile(loss = "categorical_crossentropy", optimizer = sgd, metrics = ["accuracy"])
    model.fit(np.array(trainX), np.array(TrainY), epochs = 200, batch_size = 5, verbose = 1)
    model.save("InspireModel.model")
    print("Done")

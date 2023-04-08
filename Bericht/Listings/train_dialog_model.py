import nltk
import json
import pickle
import numpy
import random

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

nltk.download('punkt')
nltk.download('wordnet')

words_for_pattern=[]
model_classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('patterns.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words_for_pattern.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in model_classes:
            model_classes.append(intent['tag'])

words_for_pattern = [lemmatizer.lemmatize(w.lower()) for w in words_for_pattern if w not in ignore_words]
words_for_pattern = sorted(list(set(words_for_pattern)))

model_classes = sorted(list(set(model_classes)))

pickle.dump(words_for_pattern, open('words_for_pattern.pkl', 'wb'))
pickle.dump(model_classes, open('model_classes.pkl', 'wb'))

training = []
output_empty = [0] * len(model_classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words_for_pattern:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[model_classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = numpy.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(numpy.array(train_x), numpy.array(train_y), epochs=500, batch_size=5, verbose=1)
model.save('dialog_model.h5', hist)
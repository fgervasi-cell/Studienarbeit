import nltk
import pickle
import numpy
import json
import random
import re

from keras.models import load_model
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('wordnet')

model = load_model('dialog_model.h5')
intents = json.loads(open('patterns.json').read())
words = pickle.load(open('words_for_pattern.pkl','rb'))
classes = pickle.load(open('model_classes.pkl','rb'))

def parse_line(line):
    reservoirs = [0] * 4
    line = re.sub(r'[,.!?]', '', line)
    words = line.split()
    for i in range(len(words)):
        if words[i] == 'Behaelter' or words[i] == 'Behälter' or words[i] == 'Reservoir':
            for x in range(i+1, len(words)):
                if words[x].isdigit():
                    index = int(words[x]) - 1
                    break
            for x in range(i-1, 0, -1):
                if words[x].isdigit():
                    reservoirs[index] = int(words[x])
                    break
    return tuple(reservoirs)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    return(numpy.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words)
    res = model.predict(numpy.array([p]))[0]
    ERROR_THRESHOLD = 0.75
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_dialog_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def get_response(msg):
    ints = predict_class(msg, model)
    if not ints:
        ints.append({"intent": "noanswer", "probability": ""})
    nums = [0] * 4
    tag = ints[0]['intent']
    if(tag == "order"):
       nums = parse_line(msg)
    res = get_dialog_response(ints, intents)
    result = ','.join(str(num) for num in nums) + '\n'
    return res, result

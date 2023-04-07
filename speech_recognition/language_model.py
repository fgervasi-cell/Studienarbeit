import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
import json
import random
model = load_model('chatbot_model.h5')
intents = json.loads(open('patterns.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def parse_line(line):
    reservoirs = [0] * 4
    words = line.split()
    for i in range(len(words)):
        if words[i] == 'Behaelter':
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

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
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
    result = ', '.join(str(num) for num in nums) + '\n'
    return res, result

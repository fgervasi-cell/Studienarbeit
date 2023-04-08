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
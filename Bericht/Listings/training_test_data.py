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
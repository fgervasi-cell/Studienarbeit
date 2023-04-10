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
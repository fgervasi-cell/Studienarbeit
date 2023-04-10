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
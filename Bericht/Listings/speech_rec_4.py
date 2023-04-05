# imports and error handling

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

while True:
    asound.snd_lib_error_set_handler(c_error_handler)
    print("Start listening...")
    with m as source:
        audio = r.listen(source)
    asound.snd_lib_error_set_handler(None)
    text = ""
    try:
        recognized_text = r.recognize_whisper(audio, language="german", model="tiny")
        text = recognized_text
        print("Recognized text: " + text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Whisper; {0}".format(e))

    if text.lower().strip().startswith("mischmaschine"):
        print("Recognized hot word. Will output answer and command.")
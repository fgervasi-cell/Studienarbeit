import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

while True:
    with m as source:
        print("Sart listening...")
        audio = r.listen(source, phrase_time_limit=5)
        print("Finished recording audio.")

    recognized_text = r.recognize_sphinx(audio, language="de-DE")
    print("Recognized text: " + recognized_text)
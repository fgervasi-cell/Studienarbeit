import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    print("Start listening...")
    audio = r.listen(source)
    text = ""
    try:
        recognized_text = r.recognize_whisper(audio, language="german", model="tiny")
        text = recognized_text
        print("Recognized text: " + text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Whisper; {0}".format(e))
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    print("Listening...")
    audio = r.listen(source)

text = r.recognize_vosk(audio, "de")
print("Vosk thinks you said: " + text)

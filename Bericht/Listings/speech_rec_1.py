import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    audio = r.listen(m)
    
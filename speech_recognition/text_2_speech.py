import pyttsx3 as tts

def speak(s):
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(s)
    engine.runAndWait()
    engine.stop()

# Sources:
# https://pypi.org/project/pyttsx3/
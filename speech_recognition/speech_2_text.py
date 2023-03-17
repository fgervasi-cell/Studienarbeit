import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        result = r.recognize_whisper(audio, language="german", model="tiny")
        print("Whisper thinks you said " + result)
        return result
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError:
        print("Could not request results from Whisper")

# Sources:
# https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
# https://github.com/openai/whisper (maybe test some other available options?)
# https://pypi.org/project/SpeechRecognition/

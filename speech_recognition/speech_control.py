import speech_recognition as sr
import pyttsx3 as tts
import serial

def language_model_stub(s):
    return s, "50,50,0,0\n"

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

while True:
    print("Start listening...")
    with m as source:
        audio = r.listen(source)
    text = ""
    try :
        recognized_text = r.recognize_whisper(audio, language="german", model="tiny")
        text = recognized_text
        print("Recognized text: " + text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Whisper; {0}".format(e))

    if text.strip().startswith("Mischmaschine"):
        print("Recognized hot word. Will output answer and command.")
        answer, cmd = language_model_stub(text)
        engine.say(answer)
        engine.runAndWait()
        engine.stop()

        #ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
        #ser.reset_input_buffer()
        #ser.write(cmd.encode("utf-8"))


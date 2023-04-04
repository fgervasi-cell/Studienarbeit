from ctypes import *
import speech_recognition as sr

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary("libasound.so")
asound.snd_lib_error_set_handler(c_error_handler)

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    asound.snd_lib_error_set_handler(c_error_handler)
    print("Start listening...")
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
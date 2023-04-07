from ctypes import *
import speech_recognition as sr

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p) #*\label{code:error_handler_begin}*)
def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary("libasound.so")
asound.snd_lib_error_set_handler(c_error_handler) #*\label{code:error_handler_end}*)

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

while True:
    asound.snd_lib_error_set_handler(c_error_handler) #*\label{code:set_handler}*)
    print("Start listening...")
    with m as source:
        audio = r.listen(source)
    asound.snd_lib_error_set_handler(None) #*\label{code:set_default_handler}*)
    text = ""
    try:
        recognized_text = r.recognize_whisper(audio, language="german", model="tiny")
        text = recognized_text
        print("Recognized text: " + text)
    except sr.UnknownValueError:
        print("Whisper could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Whisper; {0}".format(e))

    if text.lower().rstrip().startswith("mischmaschine"):
        print("Recognized hot word. Will output answer and command.")
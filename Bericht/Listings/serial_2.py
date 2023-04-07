import speech_recognition as sr
import serial
import time

def language_model_stub(s): #*\label{code:begin_model_stub}*)
    return s, "50,50,0,0\n" #*\label{code:end_model_stub}*)

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
ser.reset_input_buffer()
time.sleep(5)

while True:
    print("Start listening...")
    with m as source:
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

    if text.lower().rstrip().startswith("mischmaschine"):
        print("Recognized hot word. Will output answer and command.")
        answer, cmd = language_model_stub(text)
        ser.write(cmd.encode("utf-8")) #*\label{code:send_command}*)
        serial_answer = ser.readline().decode("utf-8").rstrip()
        print(serial_answer)


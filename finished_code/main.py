import speech_recognition as sr
import pyttsx3 as tts
import serial
import time
import language_model

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
	r.adjust_for_ambient_noise(source)

engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
# ser.reset_input_buffer()
# time.sleep(5)


while True:
	print("Start listening...")
	with m as source:
		audio = r.listen(source)
	print("Stopped listening.")

	text = ""
	try:
		if len(audio.get_raw_data()) > 10000:
			recognized_text = r.recognize_whisper(audio, language="german", model="base")
			text = recognized_text
			print("Recognized text: " + text)
	except sr.UnknownValueError:
		print("Whisper could not understand audio.")
	except sr.RequestError as e:
		print("Could not request results from Whisper; {0}".format(e))

	if text.lower().strip().startswith("mischmaschine"):
		print("Recognized hot word. Will output answer and command.")
		answer, cmd = language_model.get_response(text)
		print(answer)
		print(cmd)
		engine.say(answer)
		engine.runAndWait()
		engine.stop()

		# ser.write(cmd.encode("utf-8"))
		# serial_answer = ser.readline().decode("utf-8").rstrip()
		# print(serial_answer)


import language_model
import pyttsx3

input = "Ich haette gerne eine Mischung, die zu 50 Prozent aus Behaelter 1 und zu 50 Prozent aus Behaelter 2 besteht. Danke!"
response, result = language_model.get_response(input)
print("Response " + response)
print("Result: " + result)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say(response)
engine.runAndWait()
engine.stop()
import pyttsx3 as tts

engine = tts.init()
voices = engine.getProperty("voices") #*\label{code:get_voices}*)
engine.setProperty("voice", voices[1].id)

engine.say("Hallo Welt!")
engine.runAndWait()
engine.stop()
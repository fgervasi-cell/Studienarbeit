from speech_2_text import recognize
from language_model import get_response
from text_2_speech import speak
from serial_communication import send_to_arduino

# Let the user speak and convert the speech to text
s = recognize()
# Give this text to the language model which generates an answer and the command for the machine
answer, command = get_response(s)
# Output the answer via the speakers
speak(answer)
# Send the command to the Arduino controlling the pumps
send_to_arduino(command)

import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5) #*\label{code:open_serial}*)
ser.reset_input_buffer()
time.sleep(5) #*\label{code:sleep_serial}*)
count = 0
while True:
    ser.write("Message {0}\n".format(count).encode("utf-8"))
    line = ser.readline().decode("utf-8").rstrip() #*\label{code:read_serial}*)
    print(line)
    count += 1
    time.sleep(1)
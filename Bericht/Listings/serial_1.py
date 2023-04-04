import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
ser.reset_input_buffer()
time.sleep(5)
count = 0
while True:
    ser.write("Message {0}\n".format(count).encode("utf-8"))
    line = ser.readline().decode("utf-8").rstrip()
    print(line)
    count += 1
    time.sleep(1)
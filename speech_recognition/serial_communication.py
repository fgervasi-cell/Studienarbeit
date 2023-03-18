import serial

def serial(s):
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(s.encode('utf-8'))

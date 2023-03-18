import serial

if __name__ == '__main__':
    # Choose the same baud rate as the Arduino!!!
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    # Receive data from Arduino in infinite loop
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
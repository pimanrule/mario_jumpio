import serial
import time
try:
    ser = serial.Serial("COM6", 38400)
    i = 1
    while True:
        i += 1
        if i == 100:
            i = 0
            b = b'b'
        else:
            b = b'n'
        time.sleep(0.01)
        if (b != b'n'):
            ser.write(b)
finally:
    print("closing up shop")
    ser.close()

import serial
ser = serial.Serial("/dev/cu.usbserial-DA01GEHQ",9600)
ser.write('HelloWorld')
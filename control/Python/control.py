#Python2

#bring in necessary libraries
import serial

#open the port
ser = serial.Serial('COM3', 9600)

while 1:
    cont_data = ser.readline()
    print(cont_data)



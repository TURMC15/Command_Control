import time
import serial
def mcSerial(M1cmd, M2cmd):
    ser = serial.Serial(
        port="/dev/ttyAMA0",
        baudrate = 9600,
#    		bytesize = EIGHTBITS,
#    		parity=PARITY_NONE,
#    		stopbits=STOPBITS_ONE,
#    		timeout=None,
#    		xonxoff=False,
#    		rtscts=False,
#    		dsrdtr=False,
#    		write_timeout=None,
#    		inter_byte_timeout=None
	)

#    if (dir == "D"):
    ser.write("M1:"+M1cmd+"\r")
    ser.write("M2:"+M2cmd+"\r")


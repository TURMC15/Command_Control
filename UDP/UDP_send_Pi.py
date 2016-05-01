#!/usr/bin/env python

import socket
import math

def main():
    REC_IP = "192.168.0.100" #receiving machines IP
    REC_PORT = 8888 #port receiving machine listens on

    SERVER_ADDR = (REC_IP,REC_PORT)

    #create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    k = raw_input("Choose a Constant to scale inputs by.\nMax is 13.6\n")

    while(1):
        # msg1 and msg2 will be the inputs from the controller
        msg1 = raw_input("Left Motor\n")
        msg2 = raw_input("Right Motor\n")
        cmd1 = str(math.floor(float(k)*float(msg1)))
        cmd2 = str(math.floor(float(k)*float(msg2)))
        # strip decimal values (only integers are valid inputs)
        cmd1 = cmd1.split('.')[0]
        cmd2 = cmd2.split('.')[0]
        cmd = cmd1+"."+cmd2

        print cmd
        #send message
        sent = sock.sendto(cmd, SERVER_ADDR)

        #wait for a response
        #ack, addr = sock.recvfrom(4096)  

        #print "received %s bytes from %s as acknowledgement" % (len(ack), addr)
        #print 'Acknowledgement message is "%s"\n' % ack  


if __name__ == '__main__':
    main()

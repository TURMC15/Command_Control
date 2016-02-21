#!/usr/bin/env python

import socket

def main():
    REC_IP = "192.168.1.4" #receiving machines IP
    REC_PORT = 8888 #port receiving machine listens on

    SERVER_ADDR = (REC_IP,REC_PORT)

    #create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while(1):
        msg = raw_input("Enter Message\n")

        #send message
        sent = sock.sendto(msg, SERVER_ADDR)

        #wait for a response
        ack, addr = sock.recvfrom(4096)  

        print "received %s bytes from %s as acknowledgement" % (len(ack), addr)

if __name__ == '__main__':
    main()

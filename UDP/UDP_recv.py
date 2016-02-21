#!/usr/bin/env python

import socket

def main():

    MAX_BFR_SIZE = 4096

    MY_IP = "192.168.1.4" #this machines IP. (MUST be static)
    MY_PORT = 8888 #port this machine is listening on
    SRVR_ADDR = (MY_IP, MY_PORT)
    
    #create a socket
    srvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #bind the IP and port to the socket
    srvr.bind(SRVR_ADDR)


    ack = "your message was received"
    while(1):
        #listen for incoming messages
        data, client_addr = srvr.recvfrom(MAX_BFR_SIZE)

        #display the message
        print "received %s\n from %s" % (data, client_addr)
        print "message is %s bytes" % len(data)
        # acknowledge the data
        if data:
            sent = srvr.sendto(ack, client_addr)
            print "sent acknowledgement to %s" % ack



if __name__ == '__main__':
    main()

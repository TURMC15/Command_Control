#!/usr/bin/env python

import socket

def main():
    REC_IP = "192.168.0.100" #receiving machines IP
    REC_PORT = 8888 #port receiving machine listens on

    SERVER_ADDR = (REC_IP,REC_PORT)

    #create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    wflag = 0
    aflag = 0
    sflag = 0
    dflag = 0
    while(1):
        msg = raw_input("Enter Message\n")
        if (msg == "w"):
            wflag = wflag ^ 1
            aflag = 0
            sflag = 0
            dflag = 0
            cmd = "D1000"
        if (msg == "a"):
            wflag = 0
            aflag = aflag ^ 1
            sflag = 0
            dflag = 0
            cmd = "T-512"
        if (msg == "s"):
            wflag = 0
            aflag = 0
            sflag = sflag ^ 1
            dflag = 0
            cmd = "T512"
        if (msg == "d"):
            wflag = 0
            aflag = 0
            sflag = 0
            dflag = dflag ^ 1
            cmd = "D-1000"
        #send message
        sent = sock.sendto(cmd, SERVER_ADDR)

        #wait for a response
        #ack, addr = sock.recvfrom(4096)  

        #print "received %s bytes from %s as acknowledgement" % (len(ack), addr)
        #print 'Acknowledgement message is "%s"\n' % ack  


if __name__ == '__main__':
    main()

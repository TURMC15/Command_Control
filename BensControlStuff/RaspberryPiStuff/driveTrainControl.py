#!/usr/bin/env python
import binascii
from modules.mcSerial import mcSerial
from modules.UDP_rcv import UDP_rcv
import Queue
from threading import Thread
from BitVector import BitVector

def main():
    MULT = 10
    cmdqueue = Queue.Queue()
    rcvThread = Thread(target=UDP_rcv, args=(cmdqueue,))
    rcvThread.daemon = True
    rcvThread.start()
    while True:
        if (not(cmdqueue.empty())):
            cmd = cmdqueue.get()
            M1cmd = ord(cmd[:1])
            M2cmd = ord(cmd[1:2])

            if M1cmd > 127:
                M1cmd = -1 * (M1cmd - 128)
            if M2cmd > 127:
                M2cmd = -1 * (M2cmd - 128)

            M1cmd = M1cmd * MULT
            M2cmd = M2cmd * MULT
            print ("M1cmd = " + str(M1cmd) + " : M2cmd = " + str(M2cmd))
#            for i in range(len(cmdlist)-1):
#                mag += str(cmdlist[i+1])
#            #write the command to the UART
            mcSerial(M1cmd,M2cmd)

if __name__ == '__main__':
    main()
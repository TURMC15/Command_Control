#!/usr/bin/env python

from modules.mcSerial import mcSerial
from modules.UDP_rcv import UDP_rcv
import Queue
from threading import Thread

def main():
    cmdqueue = Queue.Queue()
    rcvThread = Thread(target=UDP_rcv, args=(cmdqueue,))
    rcvThread.daemon = True
    rcvThread.start()
    while True:
        if (not(cmdqueue.empty())):
            cmd = cmdqueue.get()
            cmdlist = cmd.split(".")

            M1cmd = cmdlist[0]
            M2cmd = cmdlist[1]
#            for i in range(len(cmdlist)-1):
#                mag += str(cmdlist[i+1])
            # write the command to the UART
            mcSerial(M1cmd,M2cmd)

if __name__ == '__main__':
    main()

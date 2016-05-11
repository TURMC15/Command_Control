import socket
import Queue
def UDP_rcv(queue):
    UDP_IP = "192.168.0.100"
    UDP_PORT = 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP,UDP_PORT))

    while True:
        data, addr = sock.recvfrom(2048)
        queue.put(data)
#        print data

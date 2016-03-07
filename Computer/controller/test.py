import socket

def test (string):
    UDP_IP = "192.168.1.4"
    UDP_PORT = 5005
    MESSAGE = string
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print "Local Hello"
    
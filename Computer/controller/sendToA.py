import socket

def sendToA (string):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    UDP_IP = "192.168.1.3"
    UDP_PORT = 5004
    MESSAGE = string
    
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    
    print "Local Hello"
    
    
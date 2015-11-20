import socket

UDP_IP = "192.168.1.141"
UDP_PORT = 5005

COMMAND = "0101010101010101111000"

print "UDP Target IP:", UDP_IP
print "UDP Target Port:", UDP_PORT
print "Command:", COMMAND

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(COMMAND, (UDP_IP,UDP_PORT))
import socket

def test (stringP, stringA):
    
    sockP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    UDP_IP_P = "192.168.1.4"
    UDP_PORT_P = 5005
    MESSAGE_P = stringP
    
    sockP.sendto(MESSAGE_P, (UDP_IP_P, UDP_PORT_P))
    sockP.close()
    UDP_IP_A = "192.168.1.3"
    UDP_PORT_A = 5004
    MESSAGE_A = stringA
    
    sockA.sendto(MESSAGE_A, (UDP_IP_A, UDP_PORT_A))
    sockA.close()
    print "Local Hello"
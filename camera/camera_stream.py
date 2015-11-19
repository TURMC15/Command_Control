'''
Created on Nov 18, 2015

@author: Ben Camp 
    by way of picamera.readthedocs.org

This goes on the pi. You run this code on the pi then try to connect to it through vcl player on your computer.
View the stream with (path to vlc)/vlc tcp/h264://(pi address: in my case it was 192.168.1.141):8000/
'''
import socket
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framefrate = 24
    
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000)) # Will need to set this to the actual address later.
    server_socket.listen(0)
    
    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format = 'h264')
        camera.wait_recording(60)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()
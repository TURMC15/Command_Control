import socket
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.brightness = 75
    camera.framerate = 24

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0',8000))
    server_socket.listen(0)

    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264', quality = 23)
        camera.wait_recording(10000)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()

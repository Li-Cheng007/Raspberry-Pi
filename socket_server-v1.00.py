#!/usr/bin/python
from __future__ import division
import socket
import sys
import time
import random
import Adafruit_PCA9685

def server_program():
    host = '10.20.30.91'
    port = 6000

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()
    try:    
        server_socket.bind((host, port))
    except socket.error:
        print('Failed to bind host and port')
        sys.exit()
    
    while True:
        try:
            print('this is ' + host + '    ' + socket.gethostbyname( host ))
            server_socket.listen(1)
            conn, address = server_socket.accept()
            print('Connection from: ' + str(address))
        except socket.error:
            print('No new connection accepted')
            sys.exit()
        data = conn.recv(1024).decode()
        def click(channel, pulse):
           pulse_length = 1000000
           pulse_length //= 60
           pulse_length //= 4096
           pulse *= 1000
           pulse //= pulse_length
           pwm.set_pwm(channel, 0, pulse)

        while data.lower().strip() == 'click3':
            print('Received from server: ' + data) 
            pwm = Adafruit_PCA9685.PCA9685() 
	   
            servo_min = 90
            servo_max = 100


            pwm.set_pwm_freq(60)
            click(15, servo_min)
            time.sleep(1)
            click(15, servo_max)
            time.sleep(1)
            break
            conn.close()


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

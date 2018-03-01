#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

MS = 17
GPIO.setmode(GPIO.BCM)
player = pyglet.media.Player();
neva = pyglet.media.load('NeverGonnaGiveYouUp.wav');
player.queue(neva);

def setup():
	GPIO.setup(MS, GPIO.IN)
	
  
def loop():
	status = 1
	while True:
		tmp = GPIO.input(MS);
		if tmp == 0:
                    player.pause();
                elif tmp == 1:
                    player.play();
		time.sleep(0.2)


import pyglet
import threading
import time


import socket
import sys

# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
sock = socket.socket();
server_address = ('172.24.66.145', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'1'
    print('sending {!r}'.format(message))
    sock.send(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while True:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()


if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	


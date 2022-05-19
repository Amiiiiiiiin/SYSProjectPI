BROADCAST_TO_PORT = 4109
from socket import *
from sense_hat import SenseHat
import time

socket = socket(AF_INET, SOCK_DGRAM)
sense = SenseHat()

socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

def up_color():
    sense.clear(255,255,0)
    data =  "yellow"
    socket.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)

def right_color():
    sense.clear(0,0,255)
    data =  "blue"
    socket.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)

def down_color():
    sense.clear(255,0,0)
    data =  "red"
    socket.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)

def left_color():
    sense.clear(0,255,0)
    data =  "green"
    socket.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)

def middle_color():
    sense.clear(255,0,255)
    data =  "magenta"
    socket.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)

def colors():
    sense.stick.direction_up = up_color
    sense.stick.direction_right = right_color
    sense.stick.direction_down = down_color
    sense.stick.direction_left = left_color
    sense.stick.direction_middle = middle_color

colors()

while True:
    for event in sense.stick.get_events():
        if event.direction == 'up' and event.action == 'pressed':
            up_color
    for event in sense.stick.get_events():
        if event.direction == 'right' and event.action == 'pressed':
            right_color
    for event in sense.stick.get_events():
        if event.direction == 'down' and event.action == 'pressed':
            down_color
    for event in sense.stick.get_events():
        if event.direction == 'left' and event.action == 'pressed':
            left_color
    for event in sense.stick.get_events():
        if event.direction == 'middle' and event.action == 'pressed':
            middle_color
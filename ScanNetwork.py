import os
import serial

# Get Device Info
'''command = "sudo pylanos/pylanos.py -H 127.0.0.1 < secret.txt"
data = os.popen(command).read()

pos = data.find("Number of")
data = data[pos+1:]'''
'''
opSys = ""
count = -1
key = "Number of"
stop = " systems detected"
while data.find(key) != -1:
    pos = data.find(key)
    end = data.find(stop, pos)
    opSys = data[pos + len(key):end]

    key = "detected: "
    stop = " ("
    pos = data.find(key)
    end = data.find(stop, pos)
    count = data[pos + len(key):end]
    data = data[end:] '''

port = "/dev/tty.usbserial-FT90AUQT"
ser = serial.Serial("/dev/tty.usbserial-FT90AUQT")

if not ser.is_open:
    ser.open()

#string = opSys + ":" + str(count) + "\r"
ser.write("Is this going to work?\r")
ser.flush()



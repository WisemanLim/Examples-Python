#Ref : https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/
#, https://circuits4you.com/2018/12/31/esp32-hardware-serial2-example/
#, https://stackoverflow.com/questions/11624190/how-to-convert-string-to-byte-array-in-python
#, https://stackoverflow.com/questions/66502267/problem-reading-data-from-esp32-to-python
#, https://github.com/Rad-hi/ESP_Python_Serial ***
#-*- coding:utf-8 -*-
#! /usr/bin/env python3
import serial
import time

MAX_BUFF_LEN = 255
SETUP = False
port = None

prev = time.time()
while(not SETUP):
    try:
        # Serial port(windows-->COM), baud rate, timeout msg
        port = serial.Serial("/dev/cu.usbserial-0001", 115200, timeout=1)
        print(port)
    except: # Bad way of writing excepts (always know your errors)
        if(time.time() - prev > 2): # Don't spam with msg
            print("No serial detected, please plug your uController")
            prev = time.time()

    if(port is not None): # We're connected
        SETUP = True

# read one char (default)
def read_ser(num_char = 1):
    string = port.read(num_char)
    return string.decode()

# Write whole strings
def write_ser(cmd):
    cmd = cmd + '\n'
    port.write(cmd.encode())

# Super loop
while(1):
    if(SETUP):
        try:
            string = read_ser(MAX_BUFF_LEN)
        except: continue

        if(len(string)):
            print(string)

        cmd = input() # Blocking, there're solutions for this ;)
        if(cmd):
            write_ser(cmd)
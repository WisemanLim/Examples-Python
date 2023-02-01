#Ref : https://techtutorialsx.com/2017/12/02/esp32-esp8266-arduino-serial-communication-with-python/
#, https://circuits4you.com/2018/12/31/esp32-hardware-serial2-example/
#-*- coding:utf-8 -*-
#!/usr/bin/python
import serial
import array

if __name__ == '__main__':
    ser = serial.Serial()
    try:
        ser.baudrate = 115200
        ser.port = '/dev/cu.usbserial-0001'
        ser.open()
    except serial.serialutil.SerialException as e:
        print(e)
    finally:
        print(ser)

    """ values = bytearray([4, 9, 62, 144, 56, 30, 147, 3, 210, 89, 111, 78, 184, 151, 17, 129])
    ser.write(values)
    total = 0
    while total < len(values):
        print(ord(ser.read(1)))
        total = total + 1
    """

    str = "Hello".encode('utf-8')
    values = bytearray(str)
    ser.write(values)
    total = 0
    while total < len(values):
        print(ord(ser.read(1)))
        total = total + 1

    ser.close()
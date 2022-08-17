# -*- coding:utf-8 -*-
# !/usr/bin/python
""" https://github.com/sn4k3/FakeRPi """
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO
from random import *
import time
import csv

def _shuffle(last_number=10):
    val = []
    for i in range(last_number):
        a = randint(1, last_number)
        while a in val:
            a = randint(1, last_number)
        val.append(a)
    print(val)
    return val

# power : 초당 전원 on 비율, direction : 방향, duration : 유지시간(1/10sec)
# PELTIER_ON/OFF(GPIO5) : H(on)/L(off), PELTIER_CON(GPIO6) : H(down)/L(up)
def control(power=100, direction=1, duration=10):
    # power와 duration을 고려하여 유지시간을 설정 : 1/10secs로 환산
    # a, b = divmod(power, duration)
    # print(a, b)
    cycle = (power // duration)
    # if (cycle == 10): cycle = 1
    print(power, cycle)
    # 해당 pin을 설정
    if (direction == 1):
        peltier_con = GPIO.LOW
        peltier_con_str = "GPIO.LOW"
    else:
        peltier_con = GPIO.HIGH
        peltier_con_str = "GPIO.HIGH"

    _range = _shuffle(10)
    for i in range(0, len(_range)):
        seq = _range[i]
        if ( seq <= cycle):
            peltier_onoff = GPIO.HIGH
            peltier_onoff_str = "GPIO.HIGH"
            # GPIO.setup(5, peltier_onoff)
            # GPIO.setup(6, peltier_con)
            time.sleep(0.1)
        else:
            peltier_onoff = GPIO.LOW
            peltier_onoff_str = "GPIO.LOW"
            # GPIO.setup(5, peltier_onoff)
            # GPIO.setup(6, peltier_con)
            time.sleep(0.1)
        print(i, seq, peltier_onoff_str, peltier_con_str)

def scenario():
    val = []
    with open("./test_scenario.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            val.append(row['Power'] + ',' + row['Direction'])
    print(val)
    return val

def main():
    import FakeRPi.Utilities
    FakeRPi.Utilities.mode = FakeRPi.Utilities.PIN_TYPE_BOARD

    pin1 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_1)
    pin2 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_2)
    pin3 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_3)
    pin4 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_4)
    pin5 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_5)
    pin6 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_6)
    pin7 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_GEN_7)
    sda1 = FakeRPi.Utilities.get_pin(FakeRPi.Utilities.PIN_GPIO_02_SDA1_I2C)

    # GPIO.setmode(GPIO.BOARD) # 라즈베리파이 보드의 핀 번호를 GPIO 번호로 쓰겠음
    GPIO.setmode(GPIO.BCM) # 회로의 GPIO 번호 그대로 쓰겠음, 일반적으로 사용하는 모드임
    GPIO.setup(pin1, GPIO.OUTPUT)
    GPIO.setup(pin1, GPIO.OUTPUT)
    GPIO.setup(pin2, GPIO.INPUT)
    GPIO.setup(pin3, GPIO.INPUT)
    GPIO.setup(pin4, GPIO.OUTPUT)
    GPIO.setup(pin5, GPIO.OUTPUT)
    GPIO.setup(pin6, GPIO.INPUT)
    GPIO.setup(pin7, GPIO.OUTPUT)

    print(GPIO.input(pin6))
    print(FakeRPi.Utilities.PIN_GPIO_GEN_6 == FakeRPi.Utilities.PIN_GPIO_25_GEN_6 == FakeRPi.Utilities.PIN_GPIO_25)  # Must be true
    GPIO.setup(pin3, GPIO.INPUT)
    GPIO.setup(pin4, GPIO.OUTPUT)
    GPIO.setup(pin5, GPIO.OUTPUT)
    GPIO.setup(pin6, GPIO.INPUT)
    GPIO.setup(pin7, GPIO.OUTPUT)

if __name__ == "__main__":
    # main()
    scval = scenario()
    # while (True):
    for i in range(0, len(scval)):
        if ( i >= 100): break
        power, direction = scval[i].split(',')
        print(power, direction)
        control(power=int(power), direction=int(direction))

"""    required = input("Enter 1.playlist to download playlist; \n"
                     "2.video to download a video \n"
                     "3.channel to download all videos from a channel \n"
                     "4.voice for only voice file \n"
                     "5.picture for picture only \n")
    if (required == "1" or required == "playlist"):
        url = input("Enter the url for whole playlist : ")
        target = input("Enter sub directory of target(only name) : ")
        conv = input("Are you want to convert mp4 to mp3(y/[N]) : ")
        if (conv.upper() == 'Y') : conv = True
        playlist(url=url, target=target, conv=conv)
    elif (required == "2" or required == "video"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        conv = input("Are you want to convert mp4 to mp3(y/[N]) : ")
        if (conv.upper() == 'Y') : conv = True
        video(url=url, target=target, conv=conv)
    elif (required == "3" or required == "channel"):
        url = input("Enter the url of the channel : ")
        target = input("Enter sub directory of target(only name) : ")
        channel(url=url, target=target)
    elif (required == "4" or required == "voice"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        video_voice_only(url=url, target=target)
    elif (required == "5" or required == "picture"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        picture_only(url=url, target=target)
    else:
        print("Invalid")
"""
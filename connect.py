#!/usr/bin/python
# -*- coding: utf-8 -*-

import smbus
import time

# Access the i2c bus
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_i2c_block_data(address, 0, value)
    #bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_i2c_block_data(address, 0, 3)
    #number = bus.read_byte(address)
    return number

while True:
    var= [2, 200, 0]
    var1= [1, 200, 0]
    var2= [3, 125, 0]
    if not var:
        continue
    writeNumber(var)
    time.sleep(3)
    writeNumber(var1)
    time.sleep(3)
    writeNumber(var2)
    print ("var = RPI: Hi Arduino, I sent you ", var)
    print ("var = RPI: Hi Arduino, I sent you ", var1)
    print ("var = RPI: Hi Arduino, I sent you ", var2)
    # sleep one second9
    time.sleep(3)
    number = readNumber()
    print ("Arduino: Hey RPI, I received a digit ", number)
    print


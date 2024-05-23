# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#sudo nano /etc/rc.local
#sudo python /home/pi/sample.py &

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import socket
import struct


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}".format("raw", "v"))

# while True:
#     print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#     print()
# 
#     time.sleep(0.5)
    
    
serverMACAddress = "40:ec:99:3e:6a:ce"
port = 5
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    #text = input()
    #if text == "quit":
    #    break
    #s.send(bytes(text, 'UTF-8'))
    s.send(bytes(str(chan.voltage), 'UTF-8'))
    time.sleep(0.5)

s.close()


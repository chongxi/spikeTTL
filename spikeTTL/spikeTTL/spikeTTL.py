# -*- coding: utf-8 -*-

"""Main module."""
import serial

class Teensy(object):
    """
    # A serial interfact to Teensy for generating x microseconds TTL (with LED at Pin13)

    - Prerequisite:
    Compile and download the /teensy/TTL/TTL.ino to the teensy 3.5/4.0

    - Example (generate a 100us pulse at Pin13):
    teensy = Teensy('/dev/ttyACM0')
    teensy.TTL(100)
    """
    def __init__(self, dev='/dev/ttyACM0'):
        super(Teensy, self).__init__()
        self.dev = dev
        self.ser = serial.Serial(self.dev)

    def TTL(self, x):
        '''
        generate a pulse with x (microseconds)
        '''
        self.ser.write(b'{}\n'.format(x))
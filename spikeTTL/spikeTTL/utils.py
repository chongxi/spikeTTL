
import serial
import os
from collections import defaultdict, deque
from time import time
import numpy as np
import matplotlib.pyplot as plt
from .plotting import colorbar


#------------------------------------------------------------------------------
# Simple serial interface for Teensy 3.5/4.0 (test pass with /teensy/TTL/TTL.ino)
#------------------------------------------------------------------------------
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
        try:
            self.ser = serial.Serial(self.dev)
        except:
            print('dev init error, please reinit by Teensy(dev)')

    def __call__(self, dev):
        self.dev = dev
        self.ser = serial.Serial(self.dev)

    def TTL(self, x):
        '''
        generate a pulse with x (microseconds)
        '''
        cmd = '{}\n'.format(x)
        self.ser.write(cmd.encode())

#------------------------------------------------------------------------------
# Simple FIFO for regular real-time input (scalar, vector, matrix or tensor)
#------------------------------------------------------------------------------

class FIFO(deque):
    '''
    A depth changeble FIFO (but assume each time receive regular data)
    Useful in real-time buffer application
    
    Example:
    -----------------
    fifo = FIFO(depth=5)
    print(fifo.shape, fifo.full)
    fifo.input(np.random.random(10,))
    print(fifo.shape, fifo.full)
    plt.imshow(fifo.numpy())    

    # to change the depth (anytime) #
    fifo.depth = 10
    
    Parameters:
    -----------------
    depth: the FIFO depth. In deque it is maxlen (must specify when init)
    shape: the FIFO numpy shape
    full:  whether the FIFO is full
    empty: whether the FIFO is empty
    
    Methods:
    -----------------
    fifo.input(var): input a scalar, vector or matrix
    fifo.mean(): mean over fifo depth
    fifo.sum():  sum over fifo depth
    '''

    def __init__(self, depth):
        self._depth = depth
        super().__init__(self, maxlen=depth)
    
    def input(self, var):
        self.append(var)
        
    def numpy(self):
        return np.array(self)
    
    def mean(self):
        return self.numpy().mean(axis=0)
    
    def sum(self):
        return self.numpy().sum(axis=0)

    def max(self):
        return self.numpy().max()

    def min(self):
        return self.numpy().min() 
    
    @property
    def shape(self):
        return np.array(self).shape
    
    @property
    def full(self):
        return len(self) == self._depth
    
    @property
    def empty(self):
        return len(self) == 0

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth):
        previous_fifo = self.numpy()
        super().__init__(self, maxlen=depth)
        self._depth = depth
        for item in previous_fifo:
            self.input(item)

    def plot(self, figsize=(5,5), colorbar_title='spike count'):
        fig, ax = plt.subplots(1,1,figsize=figsize)
        img = ax.imshow(self.numpy())
        ax.set_title('FIFO: {}x{} (depth x width)'.format(self.shape[0], self.shape[1]))
        colorbar(img, colorbar_title);
        return ax
            

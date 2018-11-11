import numpy as np
from scipy import signal
class signalGenerator:

    def __init__(self, amplitude=1, frequency=1, y_offset=0):

        self.amplitude = amplitude
        self.frequency = frequency
        self.y_offset = y_offset


    def square(self,t):
        out = self.amplitude*signal.square(2*np.pi*self.frequency*t) + self.y_offset
        return out

    def sawtooth(self,t):
        out = self.amplitude*signal.sawtooth(2*np.pi*self.frequency*t, 0.5) + self.y_offset
        return out
        
    def sin(self,t):
        out = self.amplitude*np.sin(2*np.pi*self.frequency*t) + self.y_offset
        return out

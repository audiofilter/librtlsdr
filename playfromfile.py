""" Play a WAVE file. """

import pyaudio
import struct
import sys

chunk = 1024
wf = open('audio.dat', 'rb')

p = pyaudio.PyAudio()

# open stream
stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 32000,
                output = True)

# read data
data = wf.read(chunk)

# play stream
while data != '':
    stream.write(data)
    data = wf.read(chunk)
    
stream.close()
p.terminate()


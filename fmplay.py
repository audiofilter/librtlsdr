#! /usr/bin/env python2
import socket
import struct
import time
import pyaudio
import sys
from math import floor

chunk = 4112

p = pyaudio.PyAudio()

# open stream
stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 32000,
                output = True)

class RtlTCP(object):
    def __init__(self):
        self.remote_host = "localhost"
        self.remote_port = 1234
        while True:
            try:
                self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.conn.connect((self.remote_host, self.remote_port))
                break;
            except:
                pass
            
            #self.f = open('audio.dat','wb')
        self.start = time.time()
        self.bytes = 0
    def get_data(self):
        count = 0
        while True:
	    buf = self.conn.recv(chunk)
	    if len(buf)> 0:
                #print "Got ",count,"*",len(buf)," bytes of data!!!"
                if (len(buf)> 1):
                    stream.write(buf)
                    count = count+1
                #elapsed = time.time() - self.start
                #self.bytes = self.bytes + len(buf)
                #print "16-bit words/sec = ",floor(0.5*self.bytes/elapsed)
    


        
if __name__=="__main__":
    sdr = RtlTCP()
    sdr.get_data()
    print "Done!"
    stream.close()
    p.terminate()
    

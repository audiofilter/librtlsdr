#! /usr/bin/env python2
import socket
import struct
import time
import sys

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
            
        self.f = open('audio.dat','wb')
    def get_data(self):
        count = 0
        while True:
	    buf = self.conn.recv(4112)
	    if len(buf)> 0:
                print "Got ",count,"*",len(buf)," bytes of data!!!"
                count = count+1
                if (len(buf) > 1):
                    self.f.write(buf)
                if (count == 60):
                    self.f.close()
                    return 0
    


        
if __name__=="__main__":
    sdr = RtlTCP()
    sdr.get_data()
    print "Done!"
    

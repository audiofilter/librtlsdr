import sys
import numpy, matplotlib
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt

wf = open('audio.dat', 'r')
a = numpy.fromfile(wf,dtype=numpy.int16)

plt.plot(a);
plt.show()

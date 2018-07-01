import sys
import random
import array
import numpy
from PIL import Image
#This didn't work. But then I found this article and it did
#https://github.com/python-pillow/Pillow/issues/3068

nx = 200
ny = 100
maxval = 255
j = ny + 1
i = 0
ppm_header = 'P6 {nx} {ny} {255}\n'

print "P3\n" + str(nx) + " " + str(ny) + "\n255"

image = array.array('B',[0,0,0] * nx * ny)

for j in range(ny,0,-1) :
    j = j - 1
    for i in range(0,nx) :
        r = float(i) / float(nx)
        g = float(j) / float(ny)
        b = 0.2
        ir = int(255.99*r)
        ig = int(255.99*g)
        ib = int(255.99*b)       
        print str(ir) + " " + str(ig) + " " + str(ib)

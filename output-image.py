import sys
import random
import array
import numpy
from PIL import Image, ImageDraw

#This didn't work. But then I found this article and it did
#https://github.com/python-pillow/Pillow/issues/3068

outfile = "firstimage"

nx = 200
ny = 100
maxval = 255
#j = ny + 1
j = 0
i = 0
#ppm_header = f:'P6 {nx} {ny} {255}\n'

print( "P3\n" + str(nx) + " " + str(ny) + "\n255")

img = Image.new('RGBA', (nx, ny), 'white')    
idraw = ImageDraw.Draw(img)
#for j in range(ny,0,-1) :
for j in range(0,ny) :
    for i in range(0,nx) :
        r = float(i) / float(nx)
        g = float(j) / float(ny)
        b = 0.2
        ir = int(255.99*r)
        ig = 255 - int(255.99*g)
        ib = int(255.99*b)       
        idraw.point((i,j),fill=(ir,ig,ib,255))

img.save('firstimage.png')
import sys
import random
from PIL import Image, ImageDraw
from raytracevec import vec3

outfile = "secondimage.png"

nx = 200
ny = 100
maxval = 255
#j = ny + 1
j = 0
i = 0
#ppm_header = f:'P6 {nx} {ny} {255}\n'

print( "P3\n" + str(nx) + " " + str(ny) + "\n255")

img = Image.new('RGBA', (nx, ny), 'white')   
#http://zetcode.com/python/pillow/ (Search for Drawing to Pillow image) 
idraw = ImageDraw.Draw(img)
#for j in range(ny,0,-1) :
for j in range(0,ny) :
    for i in range(0,nx) :
        col = vec3(float(i)/float(nx),float(j)/float(ny),0.2)
        #r = float(i) / float(nx)
        #g = float(j) / float(ny)
        #b = 0.2
        ir = int(255.99*col.x)
        ig = 255 - int(255.99*col.y)
        ib = int(255.99*col.z)       
        # https://pillow.readthedocs.io/en/5.2.x/reference/ImageDraw.html#methods
        idraw.point((i,j),fill=(ir,ig,ib,255))

img.save(outfile)
import sys
import random
from PIL import Image, ImageDraw
from raytracevec import vec3
from raytraceray import ray
import raytracevec

def unit_vector(other):
    if type(other) not in (vec3):
        return NotImplemented
    else:
        return other / other.length()

def color(r):
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * vec3(1.0,1.0,1.0) + t * vec3(0.5, 0.7, 1.0)

nx = 200
ny = 100

outfile = "firstraytraceimage.png"

print( "P3\n" + str(nx) + " " + str(ny) + "\n255")

lower_left_corner = vec3(-2.0,-1.0,-1.0)
horizontal = vec3(4.0,0.0,0.0)
vertical = vec3(0.0,2.0,0.0)
origin = vec3(0.0,0.0,0.0)

img = Image.new('RGBA', (nx, ny), 'white')   
#http://zetcode.com/python/pillow/ (Search for Drawing to Pillow image) 
idraw = ImageDraw.Draw(img)

for j in range(0,ny) :
    for i in range(0,nx) :
        u = float(i) / float(nx)
        v = float(j) / float(ny)
        r = ray(origin,lower_left_corner + horizontal*u + vertical*v)
        col = color(r)
        ir = int(255.99*col.x)
        ig = int(255.99*col.y)
        ib = int(255.99*col.z)

        idraw.point((i,j),fill=(ir,ig,ib,255))

mg.save(outfile)
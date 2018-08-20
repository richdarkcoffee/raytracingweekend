import sys
import random
from PIL import Image, ImageDraw
from raytracevec import vec3
from raytraceray import ray
import raytracevec

# Added this function to the main because it didn't work when included
# with import

def unit_vector(v: vec3):
    return v / v.length()
    
def dot(a: vec3, b: vec3):
    return float(a.x*b.x + a.y*b.y + a.z*b.z)

def hit_sphere(center, radius, r: vec3):
    oc = vec3(0,0,0)
    oc = r.origin() - center
    a = dot(r.direction(), r.direction())
    b = 2.0 * dot(oc, r.direction())
    c = dot(oc, oc) - radius*radius
    discriminant = b*b - 4*a*c
    return (discriminant > 0)


def color(r: vec3):
    if (hit_sphere(vec3(0,0,-1),0.5,r)):
        return vec3(1.0,0.0,0.0)
    unit_direction = unit_vector(r.direction())
    # Found out that returning unit_direction.y() means something different
    # in python than in C++. Fixed the function by removing () per blog site
    t = 0.5 *(unit_direction.y + 1.0)
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
         # Had to flip the direction of y in order to get the same picture
        ig = int(255.99*col.y)
        ib = int(255.99*col.z)

        idraw.point((i,j),fill=(ir,ig,ib,255))

img.save(outfile)
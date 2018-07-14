import sys
import random
import array
import math

class vec3:
    x = 0.0
    y = 0.0
    z = 0.0
    r = 0.0
    g = 0.0
    b = 0.0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.r = x
        self.g = y
        self.b = z

    def __add__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x+other, self.y+other, self.z+other)
        else:
            return vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __radd__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x+other, self.y+other, self.z+other)
        else:
            return vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x-other, self.y-other, self.z-other)
        else:
            return vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x*other, self.y*other, self.z*other)
        else:
            return vec3(self.x*other.x, self.y*other.y, self.z*other.z)

    def __truediv__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x/other, self.y/other, self.z/other)
        else:
            return vec3(self.x/other.x, self.y/other.y, self.z/other.z)

    def __iadd__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x+other, self.y+other, self.z+other)
        else:
            return vec3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __isub__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x-other, self.y-other, self.z-other)
        else:
            return vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __imul__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x*other, self.y*other, self.z*other)
        else:
            return vec3(self.x*other.x, self.y*other.y, self.z*other.z)

    def __itruediv__(self, other):
        if type(other) not in (vec3,int,float):
            return NotImplemented
        if type(other) in (int,float):
            return vec3(self.x/other, self.y/other, self.z/other)
        else:
            return vec3(self.x/other.x, self.y/other.y, self.z/other.z)


    def __str__(self):
        return 'vec3(%s,%s,%s)' % (self.x,self.y,self.z)

    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)

    def dot(self, other):
        return float(self.x*other.x + self.y*other.y + self.z*other.z)
    
    def cross(self, other):
        return vec3((self.y*other.z - self.z*other.y), -(self.x*other.z - self.z*other.x), (self.x*other.y - self.y*other.x))

    def make_unit_vector(self):
        k = 1.0 / math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        self.x*=k
        self.y*=k
        self.z*=k

# Not sure why we have this function. Will look at when he calls it in the code later.
    def unit_vector(other):
        if type(other) not in (vec3):
            return NotImplemented
        else:
            return other / other.length()
    
#% 	  __mod__(self, other) 	 Remainder
#< 	  __lt__(self, other) 	 Less than
# <= 	  __le__(self, other) 	 Less than or equal to
# == 	  __eq__(self, other) 	 Equal to
# != 	  __ne__(self, other) 	 Not equal to
# > 	  __gt__(self, other) 	Greater than
# >= 	  __ge__(self, other) 	 Greater than or equal to
# [index] 	  __getitem__(self, index) 	 Index operator
# in 	  __contains__(self, value) 	Check membership
# len 	__len__(self) 	 The number of elements
# str 	__str__(self) 	 The string representation

        
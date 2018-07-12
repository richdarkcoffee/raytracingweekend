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
        return vec3(self.x+other.x, self.y+other.y, self.z+other.z)

#    def __add__(self, int scalar):
#        return vec3(self.x+scalar, self.y+scalar, self.z+scalar)

    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __div__(self, other):
        return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
    def __str__(self):
        return 'vec3(%s,%s,%s)' % ('self.x','self.y','self.z')


#+ 	  __add__(self, other) 	 Addition
#* 	  __mul__(self, other) 	 Multiplication
#- 	  __sub__(self, other) 	 Subtraction
#% 	  __mod__(self, other) 	 Remainder
#/ 	  __truediv__(self, other) 	 Division
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

        
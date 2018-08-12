import sys
import random
import array
import math
import vec3 from raytracevec

class ray:
    def __init__(self, a, b):
        A = a
        B = b
    def origin(self):
        return A
    def direction(self):
        return B
    def point_at_parameter(self,t):
        return A + t*B


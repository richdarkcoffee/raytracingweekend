import sys
import random
import array
import math
from raytracevec import vec3

class ray:
    A = vec3(0.0,0.0,0.0)
    B = vec3(0.0,0.0,0.0)

    def __init__(self, a, b):
        self.A = a
        self.B = b
    def origin(self):
        return self.A
    def direction(self):
        return self.B
    def point_at_parameter(self,t):
        return self.A + t*self.B


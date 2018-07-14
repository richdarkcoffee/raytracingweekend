from raytracevec import vec3

a = 1.0
b = vec3(0,0,0)
c = vec3(2,2,2)
d = vec3(-1,1,4)

print(b+a)
print(a+b)
print(b+c)
print(c+b)
print(b.length())
print(c.length())
print(d.dot(c))
print(c.cross(d))
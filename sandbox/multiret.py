import math

def areas(r1, r2=0, r3=0, r4=0):
    return tuple([math.pi * r ** 2 for r in [r1,r2,r3,r4]])

def areas2(r1, r2=0, r3=0, r4=0):
    a1 = math.pi * r1 ** 2
    a2 = math.pi * r2 ** 2
    a3 = math.pi * r3 ** 2
    a4 = math.pi * r4 ** 2
    return a1,a2,a3,a4

print(areas(2))
print(areas2(2))
from random import random

p1 = [0, 1, 0 , 0 , 0 , 1, 1, 0, 1, 1, 0, 0]
p2 = [1, 0, 1,  1,  1,  1, 1, 1, 0, 0, 1, 1]

def probList(p1, p2 = None, inpbd = 0.5):
    for x in range(len(p1)):
        r = random()
        if r <= inpbd:
            if p2 is not None:
                p1[x] = p2[x]
            else:
                p1[x] = 1

probList(p1, p2, 0.3)
print(p1)

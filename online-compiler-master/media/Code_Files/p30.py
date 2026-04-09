                        # Cars Collision Problem

import math

C = int(input("Enter The No. Of Cars >>> "))
v= []
d = []
t = []
collide=0
        
for i in range(C):
        #x, y, element = int(input()), int(input()), int(input())
        x, y, element = input().split()
        x, y, element = [int(x), int(y), int(element)]
        v.append(element)
        element = math.sqrt( x**2 + y**2 )
        d.append(element)
        element = d[i] / v[i]
        t.append(element)

for i in range(C):
        for k in range(C):
            if k == i:
                continue
            temp = v[k] * t[i]
            if temp == d[k]:
                collide+=1

print("\n\t", collide // 2)

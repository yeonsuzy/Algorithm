tot_a, tot_b, tot_c = 0,0,0

import sys

a = int(sys.stdin.readline())
for i in range(a):
    tot_a+=int(sys.stdin.readline())
if tot_a>0:
    print("+")
elif tot_a<0:
    print("-")
else:
    print(0)    

b = int(sys.stdin.readline())
for i in range(b):
    tot_b+=int(sys.stdin.readline())
if tot_b>0:
    print("+")
elif tot_b<0:
    print("-")
else:
    print(0)
    
c = int(sys.stdin.readline())
for i in range(c):
    tot_c+=int(sys.stdin.readline())
if tot_c>0:
    print("+")
elif tot_c<0:
    print("-")
else:
    print(0)

    

import math

a,b,c = map(int,input().split())
t1 = a*b/c
t2 = a/b*c

t1 = math.trunc(t1)
t2 = math.trunc(t2)

print(max(t1,t2))
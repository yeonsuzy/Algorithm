a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

tot = sum([a,b,c,d,e,f])
tot-=min(a,b,c,d)
tot-=min(e,f)

print(tot)

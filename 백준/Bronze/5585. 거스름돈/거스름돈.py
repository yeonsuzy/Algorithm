pay = 1000 - int(input())
cnt = 0

coin = [500,100,50,10,5,1]

for c in coin:
    cnt+=pay//c
    pay = pay%c

print(cnt)
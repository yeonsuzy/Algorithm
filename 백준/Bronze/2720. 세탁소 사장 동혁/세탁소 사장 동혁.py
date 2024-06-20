t = int(input())

coin = [25, 10, 5, 1]

for _ in range(t):
    arr = []
    pay = int(input())
    
    for c in coin:
        arr.append(pay//c)
        pay%=c
        
    print(*arr)
        
    
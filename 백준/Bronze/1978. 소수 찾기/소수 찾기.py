n = int(input())

arr = list(map(int,input().split()))
tot = 0

for i in arr:
    for j in range(2,i+1):
        if i%j==0:
            if i==j:
                tot+=1
            else:
                break

print(tot)
            
    
    
arr = []
tot = 0

n = int(input())
for i in range(n):
    arr.append(int(input()))

m = int(input())
for i in range(m):
    tot+=arr[int(input())-1]
    


print(tot)
    
    
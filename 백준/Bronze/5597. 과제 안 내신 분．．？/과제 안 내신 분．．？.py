import sys

arr=[]
brr=[]

for i in range(28):
    n = int(sys.stdin.readline())
    arr.append(n)

for i in range(1,31):
    if i not in arr:
        brr.append(i)

brr.sort()

print(brr[0])
print(brr[1])
    

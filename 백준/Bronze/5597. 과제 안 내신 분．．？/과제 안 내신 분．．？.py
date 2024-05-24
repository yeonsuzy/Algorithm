# remove함수

import sys

arr=[i for i in range(1,31)]

for i in range(28):
    n = int(sys.stdin.readline())
    arr.remove(n)

arr.sort()

print(arr[0])
print(arr[1])
    

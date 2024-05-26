arr = []
mx = 0
a, b = 0, 0

import sys

for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if arr[i][j]>=mx:
            mx = arr[i][j]
            a = i
            b = j

print(mx)
print((a+1), (b+1))
            
    
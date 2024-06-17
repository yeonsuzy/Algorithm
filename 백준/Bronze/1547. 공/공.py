m = int(input())
n = 1
a, b, c = 1,2,3
for i in range(m):
    x, y = map(int, input().split())
    if x == n:
        n = y
    elif y == n:
        n = x
print(n)
    
n, x = map(int, input().split())
arr = list(map(int, input().split()))
less = []

for i in arr:
    if i < x:
        less.append(i)

for j in less:
    print(j, sep=' ')
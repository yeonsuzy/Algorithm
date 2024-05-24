n, m = map(int,input().split())
arr = []
brr = []
sm = []

for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

for i in range(n):
    b = list(map(int,input().split()))
    brr.append(b)        

for i in range(n):
    for j in range(m):
        print(arr[i][j]+brr[i][j], end=' ')
    print()
        
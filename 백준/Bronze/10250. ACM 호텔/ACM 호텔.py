t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    f = (n-1)%h +1
    r = (n-1)//h+1
    
    print(f*100+r)
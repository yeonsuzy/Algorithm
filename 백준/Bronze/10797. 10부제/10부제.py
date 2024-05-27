d = int(input())
c = list(map(int,input().split()))
cnt = 0

for i in range(5):
    if d == c[i]:
        cnt+=1
        
print(cnt)
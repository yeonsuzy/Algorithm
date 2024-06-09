n = int(input())
k = input()
cnt1, cnt2 = 0,0

for i in range(n):
    if int(k[i])%2 == 1:
        cnt1+=1
    else:
        cnt2+=1

if cnt1>cnt2:
    print(1)
elif cnt1<cnt2:
    print(0)
else:
    print(-1)


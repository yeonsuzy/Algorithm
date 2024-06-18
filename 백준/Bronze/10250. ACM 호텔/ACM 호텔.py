t = int(input())
f, r = 0, 0

for i in range(t):
    h, w, n = map(int, input().split())

    f = n%h
    r = (n//h)+1

    if f==0:
        f = h    # 꼭대기층일 경우
        r = n//h

    if r>=10:
        print(str(f)+str(r))
    else:
        print(str(f)+str(0)+str(r))

l, p = map(int, input().split())
news = list(map(int, input().split()))
cnt = l*p
wrong = [0]*5

for i in range(5):
    if news[i]!=cnt:
        wrong[i] = news[i] - cnt

for i in wrong:
    print(i, end = ' ')
        

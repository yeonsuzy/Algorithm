n = int(input())
arr = []
cnt = 1

while True:
    try:
        a = int(input())
        if a==1:
            break
        cnt+=(a-1)
    except:
        break
    

print(cnt)
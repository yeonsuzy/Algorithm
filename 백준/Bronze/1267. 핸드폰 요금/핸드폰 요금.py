n = int(input())
arr = list(map(int, input().split()))
y,m = 0,0

# 영식
for i in range(n):
    y+=int((arr[i]//30)+1)*10
    m+=int((arr[i]//60)+1)*15

if y<m:
    print("Y", y)
elif y>m:
    print("M", m)
else:
    print("Y M", y)
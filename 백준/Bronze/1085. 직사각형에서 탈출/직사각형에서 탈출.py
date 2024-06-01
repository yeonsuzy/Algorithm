x,y,w,h=map(int,input().split())
x_s = 0
y_s = 0

if x<(w/2):
    x_s = x
else:
    x_s = w-x

if y<(h/2):
    y_s = y
else:
    y_s = h-y
    
if x_s<y_s:
    print(x_s)
else:
    print(y_s)
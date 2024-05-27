a = int(input())
b = int(input())
c = int(input())
sm = a+b+c

if sm==180:
    if a==b==c:
        print("Equilateral")
    elif a!=b and b!=c and a!=c:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")
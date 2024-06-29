while 1:
    num = input()
    
    if num=='0':
        break
    else:
        inner = 1
        for i in num:
            if i=='1':
                inner = inner+2+1
            elif i=='0':
                inner = inner+4+1
            else:
                inner = inner+3+1
        print(inner)
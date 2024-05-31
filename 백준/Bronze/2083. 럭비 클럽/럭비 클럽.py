while True:
        a, b, c = input().split()
        b = int(b)
        c = int(c)
        p = ''
        if a == '#':
            break
        if b>17 or c>=80:
            p = 'Senior'
        else:
            p = 'Junior'
        print(a, p)

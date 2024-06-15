n= input()

#b가 10일 때의 경우를 처리해준다.
if n[-2] + n[-1] == "10":  

    print( int(n[:-2]) + 10)


#그 외의 모든 상황은 b는 일의자리다.

else:

    print( int(n[:-1]) + int(n[-1]) )
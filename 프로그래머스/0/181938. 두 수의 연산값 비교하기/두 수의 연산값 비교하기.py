def solution(a, b):
    str(a)+str(b)

    if int(solution(a,b)) > (2*a*b):
        return int(solution(a,b))
    elif int(solution(a,b)) < (2*a*b):
        return (2*a*b)
    else:
        return int(solution(a,b))
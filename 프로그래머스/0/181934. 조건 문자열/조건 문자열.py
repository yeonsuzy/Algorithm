def solution(ineq, eq, n, m):
    answer = ineq + eq
    if answer == "<=":
        if n<=m:
            return 1
        else:
            return 0
    elif answer == ">=":
        if n>=m:
            return 1
        else:
            return 0
    elif answer == "<!":
        if n<m:
            return 1
        else:
            return 0
    elif answer == ">!":
        if n>m:
            return 1
        else:
            return 0
    
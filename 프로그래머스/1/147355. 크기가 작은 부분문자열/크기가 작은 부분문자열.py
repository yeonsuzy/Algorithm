def solution(t, p):
    answer = 0
    s = len(str(p))
    arr = []
    for i in range(0,len(str(t))-s+1):
        arr.append(int(str(t)[i:i+s]))
    for i in arr:
        if i<=int(p):
            answer+=1
    return answer
def solution(seoul):
    answer=''
    cnt=0
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            cnt=i
    answer += '김서방은 '
    answer+=str(cnt)
    answer+='에 있다'
    return answer
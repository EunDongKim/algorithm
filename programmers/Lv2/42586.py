import math

def solution(progresses, speeds):
    t = []
    answer = []
    
    for i in range(len(progresses)):
        t.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    ans = 0
    standard = t[0]

    for i in range(len(t)):
        if t[i] <= standard:
            ans += 1
        else :
            standard = t[i]
            answer.append(ans)
            ans = 1
    else : answer.append(ans)
    
    return answer

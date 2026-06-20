def solution(n, lost, reserve):
    
    # -1은 없는 학생 0은 자신의 것만 1는 reserve 가지고 있는 학생
    s = [0]*n
    for l in lost:s[l-1] -= 1
    for r in reserve:s[r-1] += 1
    
    for i in range(n):
        if s[i] == -1:
            if i != 0 and s[i-1] == 1:
                s[i-1] -= 1
                s[i] += 1
            elif i != len(s)-1 and s[i+1] == 1:
                s[i+1] -= 1
                s[i] += 1
    
    answer = 0
    for i in s:
        if i != -1: answer += 1
    return answer

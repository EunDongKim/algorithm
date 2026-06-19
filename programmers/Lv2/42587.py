def solution(p, location):
    answer = 1
    while True:
        if p[0] < max(p):
            p.append(p.pop(0))         
            if location == 0 :
                location = len(p) -1
            else : location -= 1
        elif p[0] == max(p):
            if location == 0 :
                return answer
            else:
                p.pop(0)
                answer += 1
                location -= 1

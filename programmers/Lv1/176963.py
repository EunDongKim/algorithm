def solution(name, yearning, photo):
    
    d = dict(zip(name, yearning))
    answer = []
    
    for shot in photo:
        score = 0
        for person in shot:
            try :
                score += d[person]
            except : continue
        answer.append(score)
    return answer
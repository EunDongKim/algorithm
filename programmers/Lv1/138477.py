def solution(k, score):
    a = []
    answer = []
    for i in score:
        if len(a) != k or min(a) <= i:
            a.append(i)
            a.sort(reverse=True)
            if len(a) > k:
                a.pop()
        answer.append(a[-1])
    return answer

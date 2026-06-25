def solution(dirs):
    answer = 0
    ud, lr = 0, 0
    visited = []
    for d in dirs:
        if [ud,lr,d] not in visited:
            visited.append([ud,lr,d])
            if d == 'U' and ud != 5:
                answer += 1
                ud += 1
                visited.append([ud,lr,'D'])
            elif d == 'D' and ud != -5:
                answer += 1
                ud -= 1
                visited.append([ud,lr,'U'])
            elif d == 'R' and lr != 5:
                answer += 1
                lr += 1
                visited.append([ud,lr,'L'])
            elif d == 'L' and lr != -5:
                answer += 1
                lr -= 1
                visited.append([ud,lr,'R'])
        else :
            if d == 'U' and ud != 5:
                ud += 1
            elif d == 'D' and ud != -5:
                ud -= 1
            elif d == 'R' and lr != 5:
                lr += 1
            elif d == 'L' and lr != -5:
                lr -= 1
    return answer

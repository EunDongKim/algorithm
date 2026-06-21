def solution(array, commands):
    answer= []
    for c in commands:
        temp = array.copy()
        temp = temp[c[0]-1:c[1]]
        temp.sort()
        answer.append(temp[c[2]-1])
    return answer

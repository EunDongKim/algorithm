def solution(operations):
    answer = []
    for o in operations:
        if o[0] == 'I':
            answer.append(int(o[2:]))
        elif len(answer) == 0 : 
            continue
        elif o == 'D 1' :
            answer.remove(max(answer))
        else : 
            answer.remove(min(answer))
        
    return list((max(answer), min(answer))) if len(answer) != 0 else [0, 0]

def solution(keymap, targets):
    d = {}
    t = set()
    answer = []
    for target in targets:
        for alphabet in target:
            t.add(alphabet)
            
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] in t and (keymap[i][j] not in d or j+1 < d[keymap[i][j]]):
                d[keymap[i][j]] = j+1
    
    for i in range(len(targets)):
        cnt = 0
        for j in range(len(targets[i])):
            if targets[i][j] not in d:
                cnt = -1
                break
            else :
                cnt += d[targets[i][j]]
        answer.append(cnt)
        
    return answer

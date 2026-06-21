def solution(s):
    cnt = 0
    for p in s:
        if p == '(':
            cnt += 1
        elif p == ')':
            cnt -= 1
        if cnt < 0: return False
    if cnt == 0 : return True
    else : return False

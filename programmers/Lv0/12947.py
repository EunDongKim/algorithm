def solution(x):
    
    answer = True
    string_x = str(x)
    sum_x = 0
    
    for c in string_x:
        sum_x += int(c)
        
    if x % sum_x != 0:
        answer = False
    
    return answer
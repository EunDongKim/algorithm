def solution(num, total):
    
    # num이 홀수일 때
    if num % 2 != 0:
        center = total // num
        answer = [center]*num
        centerindex = num//2
    
    # num이 짝수일 때
    else :
        center = total // (num//2)
        x = (center - 1) // 2
        answer = [x] * num
        centerindex = (num // 2) -1
        
    for i in range(num):
        answer[i] -= centerindex - i
    
    return answer

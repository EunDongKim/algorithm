def solution(n,a,b):
    answer = 1

    while True:
        if abs(a-b) == 1 and max(a,b) % 2 == 0 : return answer
        if a % 2 == 1 : a += 1
        if b % 2 == 1 : b += 1
        
        a = a // 2
        b = b // 2
        answer += 1

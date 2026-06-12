def solution(n):
    answer = 0
    
    for i in range(3,n+1):
        if not isitprime(i):
            print(i)
            answer += 1
    return answer

def isitprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        

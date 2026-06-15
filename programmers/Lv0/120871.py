def solution(n):
    numberof3x =  []
    num = 1
    
    while len(numberof3x) < n:
        if num %3 != 0 and not '3' in str(num):
            numberof3x.append(num)
        num += 1
        
    return numberof3x[n-1]

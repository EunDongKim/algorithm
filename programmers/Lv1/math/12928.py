def solution(n):
    array = []
    
    for i in range(1, int(n ** 0.5)+1):
        if n / i - n//i == 0:
            array.append(i)
            
    for i in range(len(array)):
        if array[i] ** 2 != n :array.append(n//array[i])
    
    return sum(array)

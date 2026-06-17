def solution(nums):
    p = len(nums) // 2 
    answer = 0
    d = {}
    
    for n in nums:
        if n in d:
            d[n] += 1
        else :
            d[n] = 1
    
    v = list(d.values())
    if len(v) - p > 0:
        return p
    else :
        return len(v)

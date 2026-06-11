def solution(sides):
    
    maxside = max(sides)
    minside = min(sides)
    setside = set()
    
    # max가 가장 긴 변일때 max-min < ? < max
    for i in range(maxside-(minside+1), maxside):
        if minside + i > maxside :
            setside.add(i)
            
    # ? 가 max와 길이가 같을 때
    setside.add(maxside)
    
    # ? 가 min과 길이가 같을 때
    if minside * 2 > maxside : setside.add(minside)
    
    # ? 가 가장 긴 변일때 max + min > ? > max
    for i in range(maxside, maxside+minside):
        setside.add(i)
    
    return len(setside)

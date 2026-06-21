def solution(s, skip, index):
    alphabet = []
    answer = ""
    for i in range(ord('a'), ord('z') + 1) : 
        alphabet.append(chr(i))
    
    for i in skip : 
        alphabet.remove(i)
        
    for i in range(len(s)):
        answer += alphabet[(alphabet.index(s[i])+index)%len(alphabet)]
        
    return answer

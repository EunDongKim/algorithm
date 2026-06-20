def solution(s):
    answer = []
    a = ''
    for c in s:
        answer.append(ord(c))
    answer.sort(reverse = True)
    for i in range(len(answer)):
        a += chr(answer[i]) 
    return a

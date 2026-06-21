def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            answer += chr((ord(i)-97+n)%26+97)
        elif ord(i) >= 65 and ord(i) <= 90:
            answer += chr((ord(i)-65+n)%26+65)
        else: answer += i
    return answer

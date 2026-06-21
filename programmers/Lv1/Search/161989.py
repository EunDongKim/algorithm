def solution(n, m, section):
    answer = 0
    section.reverse()
    while len(section) != 0:
        painting = section[-1]+m-1
        while len(section) != 0 and painting >= section[-1]:
            section.pop()
        answer += 1
    return answer

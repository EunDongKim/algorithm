def solution(answers):
    n = len(answers) // 10 + 1
    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] * n
    b = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] * n
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *n
    cnt_a, cnt_b, cnt_c = 0, 0, 0
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == a[i] : cnt_a += 1
        if answers[i] == b[i] : cnt_b += 1
        if answers[i] == c[i] : cnt_c += 1
    
    cnt = [cnt_a, cnt_b, cnt_c]
    cnt_winner = max(cnt)
    for i in range(3):
        if cnt[i] == cnt_winner:
            answer.append(i+1)
    return answer

def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(i+1,n):
            cnt += 1
            if prices[i] > prices[j]: break
        answer[i] = cnt
    return answer

'''
- 아이디어
- numbers[0]부터 [-1]까지 +인 경우와 -인 경우를 나눠 DFS를 적용시켜 푼다
- +인 경우와 -인 경우 각각 스택에 넣는다
- idx가 -1이 된 경우 총합이 target과 같은 경우 ans를 1 증가시킨다

- 시간복잡도
- O(V+E) = 2^n = 2^20 = 100만번

- 자료구조
- 스택 = int[][]
'''
def solution(numbers, target):
    l = len(numbers)
    times = [1,-1]
    stack= [[0,0]]
    answer = 0  
    
    while stack:
        idx, res = stack.pop()
        if idx != l:
            for i in range(2):
                r = res
                r += numbers[idx]*times[i]
                stack.append([idx+1,r])
        else :
            if res == target:
                answer += 1
    return answer

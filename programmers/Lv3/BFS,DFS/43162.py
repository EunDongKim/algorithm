'''
- 아이디어
1. n개의 컴퓨터를 각각 돌면서 네트워크가 해당 컴퓨터만 연결됐는 지 확인한다
2. 다른 컴퓨터와 연결된 경우 DFS알고리즘을 통해 다른 연결된 컴퓨터를 확인한다
3. boolean 타입을 통해 방문 여부를 체크한다
4. DFS알고리즘까지 끝난다면 answer을 1 증가시킨다

- 시간복잡도
O(V^2) = V^2 = 200 *200 = 40000 

- 자료구조
stack = int[][]
visited = bool[]
'''
def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def DFS(idx):
        stack = []
        for i in range(n):
            if i != idx and not visited[i] and computers[idx][i] == 1:
                stack.append(i)
        while stack:
            idx = stack.pop()
            for i in range(n):
                if i != idx and not visited[i] and computers[idx][i] == 1:
                    stack.append(i)
                    visited[i] = True
            
            
    for i in range(n):
        if visited[i] == False:
            DFS(i)
            answer += 1
    return answer

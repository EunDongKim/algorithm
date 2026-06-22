'''
- 아이디어
1. 이중 for문을 돌면서 숫자를 찾는다
2. 숫자를 찾으면 아래우 BFS 알고리즘으로 연결된 숫자를 찾는다
    2-1. BFS(좌표, 각 숫자의 합) 로 정의한다
3. check 리스트를 통해 BFS로 확인한 곳을 체크한다
4. 무인도 숫자의 합을 리스트에 모아 놓는다.
5. sort를 통해 정렬 후 출력한다

- 시간 복잡도
- O(V+E) = V + E = V + 4V = 5V = 5(100*100) = 50000

- 자료구조
- BFS 알고리즘에 사용될 Queue : int[][]
- 4번을 위한 int[]
- chk = bool[][]
'''


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    chk = [[False] * m for _ in range(n)]
    dy = [0,1]
    dx = [1,0]
    
    def BFS(y,x):
        q = [[y,x]]
        ans = 0
        chk[y][x] = True
        while q:
            cy, cx = q.pop()
            ans += int(maps[cy][cx])
            for i in range(2):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0 <= ny < n and 0<=nx<m:
                    if maps[ny][nx] != 'X' and chk[ny][nx] == False:
                        chk[ny][nx] = True
                        q.append([ny,nx])
        return ans
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and chk[i][j] == False:
                answer.append(BFS(i, j))
    if not answer: return [-1]
    answer.sort()
    return answer

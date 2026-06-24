'''
- 아이디어
목표 1 : 레버로 가는 가장 빠른 경로를 BFS알고리즘을 통해 찾는다
    방문한 장소는 visited를 true로 바꾼다
목표 2 : 레버에서 출구로 가는 가장 빠른 경로를 BFS알고리즘을 통해 찾는다
    visited를 초기화한 후 레버가 있는 장소를 True로 바꾼다.
    추후 목표 1과 같이 방문한 장소는 true로 바꾼다

- 시간복잡도
O(N*M) = N*M*4*2 = 80000
- 자료구조
queue = int[][] visited = bool[][]
'''

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    visited = [[False] * m for _ in range(n)]
    temp = [[False] * m for _ in range(n)]
    def BFS(x, y, t, o):
        q = [[x,y,t,o]]
        while q:
            x, y, t, o= q.pop(0)
            t += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]  
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X' and not visited[ny][nx]:
                    if maps[ny][nx] == o:
                        return [nx, ny, t]
                    else:
                        q.append([nx,ny,t,o])
                        visited[ny][nx] = True

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                visited[i][j] = True
                res = BFS(j,i,0,'L')
                if res : 
                    visited = temp
                    answer += res[2]
                    visited[res[1]][res[0]] = True
                    res = BFS(res[0],res[1],0,'E')
                    if res :
                        answer += res[2]
                        return answer
                return -1

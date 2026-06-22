'''
- 아이디어
1. 시작점에서 위 아래 양옆을 확인해 값이 1이면 chk가 false면 True로 바꾸고 큐에 넣는다.
2. 여러 갈래길이 나올 경우 BFS를 통해 최단 거리를 구한다.
3. 모든 경우의 수 중 가장 작은 값을 return한다
    2.1. 만약 경우의 수가 없다면 -1을 return한다

- 시간복잡도
O(V+E) = V + E = V + 4V = 5V = 5(100*100) = 50000

- 자료구조
queue = int[][]
chk = bool[][]
'''
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    chk = [[False]*m for _ in range(n)]
    
    x, y = 0, 0
    dy = [-1,0,0,1]
    dx = [0,-1,1,0]
    
    
    q = [[y,x, 1]]
    chk[0][0] = True
    while q:
        cy, cx, t = q.pop(0)
        t += 1 
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not chk[ny][nx] and maps[ny][nx] :
                    if ny == n-1 and nx == m-1: return t
                    
                    q.append([ny,nx,t])
                    chk[ny][nx] = True
                    
    return -1

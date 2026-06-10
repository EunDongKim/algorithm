def solution(park, routes):
    
    # 시작 지점 찾기
    answer = findS(park)
    for route in routes:
        
        op = route[0]
        n = int(route[2])
        moveflag = False
        x, y = answer[1], answer[0]
        temp = answer
        
        # 공원을 벗어나는지 확인하기
        if op == "N" and answer[0] - n >= 0 :
            moveflag = True
            ycase = -1
            xcase = 0
        elif op == "W" and answer[1] - n >= 0 :
            moveflag = True
            ycase = 0
            xcase = -1
        elif op == "S" and answer[0] + n < len(park) : 
            moveflag = True
            ycase = 1
            xcase = 0
        elif op == "E" and answer[1] + n < len(park[0]) :
            moveflag = True
            ycase = 0
            xcase = 1
        
        # 장애물이 있는지 확인하기
        if moveflag:
            for i in range(n):
                if park[y+(ycase*(i+1))][x+(xcase*(i+1))] == 'X':
                    moveflag = False
                    break
                elif i == n-1 :  # 장애물이 없으면 이동하기
                    answer[0] = y+(ycase*(i+1))
                    answer[1] = x+(xcase*(i+1))
        print(answer)
    return answer

def findS(park):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                return [i,j]

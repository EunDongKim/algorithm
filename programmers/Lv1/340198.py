def solution(mats, p):
    mats.sort(reverse= True)
    for m in mats:
        x, y = 0, 0
        maxofx = len(p[0])-m
        maxofy = len(p)-m
        while y <= maxofy and x <= maxofx:
            if p[y][x] == "-1":
                if findarea([row[x:] for row in p[y:]], m):
                    return m
            if x >= maxofx:
                x = 0
                y += 1
            else : x+= 1
    return -1

def findarea(arr,size):
    for i in range(size):
        for j in range(size):
            if arr[i][j] != "-1":
                return False
    return True

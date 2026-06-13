def solution(wallpaper):
    top, bottom, left, right = -1, -1, -1, -1
    rowcount, itemcount = 0, 0
    
    for row in wallpaper:
        for item in row:
            if item == '#':
                if top == -1:
                    top = rowcount
                if left == -1 or itemcount < left :
                    left = itemcount
                if bottom == -1 or rowcount > bottom:
                    bottom = rowcount
                if right == -1 or itemcount > right:
                    right = itemcount 
            itemcount += 1
        itemcount = 0
        rowcount += 1
    
    return [top,left,bottom+1,right+1] # bottom right는 칸의 오른쪽 밑을 포인팅 해야하므로 +1을 해줘야함
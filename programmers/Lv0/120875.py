def solution(dots):
    a = []
    maindot = 0
    while maindot != len(dots):
        for i in range(maindot+1, len(dots)):
            x=dots[i][0]-dots[maindot][0]
            y=dots[i][1]-dots[maindot][1]
            a.append([y/x, maindot,i])
        maindot += 1
    
    cur = 0
    while cur != len(a):
        for i in range(cur+1, len(a)):
            if a[cur][0] == a[i][0] and not a[cur][1] in a[i][1:] and not a[cur][2] in a[i][1:] :
                return 1
        cur += 1
    return 0

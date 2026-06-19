def solution(brown, yellow):
    x = 3
    y = 3
    while True:
        if x*y == brown + yellow and 2*x+2*y-4 == brown:
            return [x,y]
        elif x > y:
            y += 1
        else :
            x += 1
            y = 3

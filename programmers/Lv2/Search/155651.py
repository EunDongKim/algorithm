'''
00:00 형태의 23*60개 딕셔너리를 만든다. book_time 내 시간들은 딕셔너리에서 +1이 된 후 maxvalue값을 출력한다.
'''
def solution(book_time):
    t = [0] * 23 * 60
    
    def tosecond(s):
        return int(s[0:2]) * 60 + int(s[3:])
    
    for i in book_time:
        start = i[0]
        end = i[1]
        for j in range(tosecond(start), tosecond(end)+10):
            if j >= 23*60: break
            t[j] += 1
    
    return max(t)

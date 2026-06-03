def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        limit = schedules[i]+10
        day = startday
        flag = False
        if limit % 100 >= 60: limit+=40
        for t in timelogs[i]:
            if day >= 6:
                day = day % 7 + 1
                continue
            day += 1
            if limit < t :
                flag = True
                break
        if flag == False : answer += 1
    return answer
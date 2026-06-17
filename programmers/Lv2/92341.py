def solution(fees, records):
    timelist = []
    answer = []
    car = {}

    for record in records:
        temp = list(record.split(' '))
        try :
            car[temp[1]] = car[temp[1]] + '/' + temp[0] + temp[2]
        except :
            car[temp[1]] = temp[0] + temp[2]
            
    sortedcar = dict(sorted(car.items(), key = lambda item : item[0]))

    # 차번호마다 시간 구하기
    for key in sortedcar.keys():
        temp = list(sortedcar[key].split('/'))
        time = 0
        INtime = 0
        for i in temp:
            if i[-1] == 'N':
                INtime = i[0:5]
            else :
                time += (int(i[0:2]) * 60 + int(i[3:5])) - (int(INtime[0:2]) * 60 + int(INtime[3:5]))
        if temp[-1][-1] == 'N':
            time += 23 * 60 + 59 - (int(INtime[0:2]) * 60 + int(INtime[3:5]))
        timelist.append(time)

    # 시간마다 요금 구하기
    for time in timelist:
        fee = fees[1]
        time -= fees[0]
        
        if time > 0 : 
            fee += (time // fees[2]) * fees[3]
            if time // fees[2] != time / fees[2]:
                fee += fees[3]
        
        answer.append(fee)
    return answer

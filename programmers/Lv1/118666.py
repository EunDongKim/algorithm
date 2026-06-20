def solution(survey, choice):
    r = {'RT' : 0, 'CF' : 0, 'JM' : 0, 'AN' : 0}
    
    for i in range(len(survey)):
        if survey[i][0] in 'AN':
            if survey[i][0] == 'A':
                r['AN'] -= choice[i] - 4
            else : 
                r['AN'] += choice[i] - 4
            
        elif survey[i][0] in 'CF':
            if survey[i][0] == 'C':
                r['CF'] -= choice[i] - 4
            else : 
                r['CF'] += choice[i] - 4
            
        elif survey[i][0] in 'JM':
            if survey[i][0] == 'J':
                r['JM'] -= choice[i] - 4
            else : 
                r['JM'] += choice[i] - 4
                
        else : 
            if survey[i][0] == 'R':
                r['RT'] -= choice[i] - 4
            else : 
                r['RT'] += choice[i] - 4
            
    answer = ''
    for k, v in r.items():
        if r[k] >= 0 : answer += k[0]
        else : answer += k[1]
        
    return answer

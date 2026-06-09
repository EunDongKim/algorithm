def solution(players, callings):
    
    dict_players = {index: value for value,index in enumerate(players)}
    
    for call in callings:
        
        # '불린 player'와 '불린 player를 앞선 player' 찾기
        cur = dict_players[call] #int
        prev = players[cur-1] #str
        
        # 딕셔너리 순위 최신화
        dict_players[call] -= 1
        dict_players[prev] += 1
        
        # 리스트 순위 최신화
        temp = players[cur] 
        players[cur] = players[cur-1]
        players[cur-1] = temp
        
    return players

def solution(bandage, health, attacks):
    maxhealth = health
    for i in range(len(attacks)-1):
        
        health -= attacks[i][1]
        if health <= 0 : return -1
    
        # 공격 간 시간 카운트
        time = attacks[i+1][0]-attacks[i][0]-1 
        
        # 붕대감기로 회복
        health += time * bandage[1] + (time // bandage[0]) * bandage[2]
        
        # 최대 체력 확인
        if health >= maxhealth : health = maxhealth
    health -= attacks[-1][1]
    return health if health > 0 else -1

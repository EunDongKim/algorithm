def solution(spell, dic):
    
    spelldictionary = {chr(i+97) : False for i in range(26)}
    for alphabet in spell:
        spelldictionary[alphabet] = True
    
    for sentence in dic:
        # dic의 원소가 나올 때마다 사용 유무를 따질 수 있게 얕은 복사
        temp = spelldictionary.copy() 
        
        # for-else 문을 통해 모든 알파벳을 검토한 경우를 분기하기
        for alphabet in sentence:
            if temp[alphabet] != True: break
            else : temp[alphabet] = False
            
        else :
            # 원소를 모두 사용 안한 경우 거르기
            if sum(temp.values()) == 0: 
                return 1
    
    # 모든 sentence 조사 했을 때 안나올 경우 return하기
    return 2
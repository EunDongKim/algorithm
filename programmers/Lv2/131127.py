def solution(want, number, discount):
    wantlist = {want[i]:number[i] for i in range(len(want))}
    ans = 0
    for i in range(len(discount)-9):
        
        temp = wantlist.copy()
        
        for j in range(10):
            
            if discount[i+j] in temp.keys() and temp[discount[i+j]] != 0:
                temp[discount[i+j]] -= 1
            
            if sum(temp.values()) == 0:
                print(i)
                ans += 1
                
    return ans

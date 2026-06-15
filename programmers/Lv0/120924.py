def solution(common):
    return common[-1]*(common[-2]//common[-3]) if common[-2]+(common[-2]-common[-3]) != common[-1]\
    else (common[-2]-common[-3])+common[-1]

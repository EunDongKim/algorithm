def solution(data, ext, val_ext, sort_by):
    
    match ext:
        case "code" : index = 0
        case "date" : index = 1
        case "maximum" : index = 2
        case "remain" : index = 3
        
    answer = []
    for i in data:
        if i[index] < val_ext : answer.append(i)
        
    match sort_by:
        case "code" : index = 0
        case "date" : index = 1
        case "maximum" : index = 2
        case "remain" : index = 3
    return sorted(answer, key=lambda item:item[index])
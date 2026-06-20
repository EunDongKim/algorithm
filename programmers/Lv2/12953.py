def solution(arr):
    a = arr.copy()
    
    def times(arr):
        for i in range(len(arr)):
            if arr[i] == min(arr):
                arr[i] += a[i]
                return arr
            
    while True :
        if max(arr) == min(arr) :
            return arr[0]
        else:
            arr = times(arr)

def solution(arr):
    answer = []
    
    now_num = arr[0]
    answer.append(now_num)
    
    for num in arr:
        if now_num != num:
            answer.append(num)
            now_num = num
        

    return answer
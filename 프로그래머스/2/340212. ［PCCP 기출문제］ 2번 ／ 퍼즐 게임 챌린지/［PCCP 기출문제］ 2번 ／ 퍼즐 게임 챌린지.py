def solution(diffs, times, limit):
    
    start = 1
    end = max(diffs)
    
    
    while start < end:
        mid = (start + end) // 2
        tmp_limit = 0
        
        
        for i, diff in enumerate(diffs):
            
            # time_prev 값
            if i == 0:
                time_prev = 0
            else: 
                time_prev = times[i-1]
                
            # 시간 계산
            time_cur = times[i]
            
            if mid >= diff:
                tmp_limit += time_cur
            else:
                tmp_limit += (diff - mid) * (time_cur + time_prev) + time_cur
            
        # 현재 limit 값 
        if tmp_limit <= limit:
            end = mid
        else:
            start = mid + 1

    return start
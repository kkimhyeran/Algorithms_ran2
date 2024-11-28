def solution(n, lost, reserve):
    
    lost_new = list(set(lost) - set(reserve))
    reserve_new = list(set(reserve) - set(lost))
    
    # 2. 체육복 빌릭
    cnt = 0
    for l in lost_new:
        if l - 1 in reserve_new:
            reserve_new.remove(l-1)
            cnt += 1
        elif l + 1 in reserve_new:
            reserve_new.remove(l+1)
            cnt += 1
            
    return n - len(lost_new) + cnt
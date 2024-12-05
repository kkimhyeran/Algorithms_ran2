from collections import deque
def solution(queue1, queue2):
    
    total = sum(queue1) + sum(queue2)
    
    if total % 2 == 0 :
        target_val = total // 2
    else:
        return -1
    
        
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    n = len(queue1)
    chk = 0
    
    while chk < n*3:
        chk += 1
        
        if q1_sum == target_val:
            return chk-1
        
        elif q1_sum > target_val:
            val = queue1.popleft()
            queue2.append(val)
            q1_sum -= val
            q2_sum += val
        
        elif q1_sum < target_val:
            val = queue2.popleft()
            queue1.append(val)
            q2_sum -= val
            q1_sum += val
            
        
    return -1
from collections import deque
def solution(queue1, queue2):
    
    target_val = (sum(queue1) + sum(queue2)) / 2
    print(target_val)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    return 0
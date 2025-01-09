def solution(order):
    
    idx = 0
    now_box = 0
    stack = []
    while idx < len(order):
        if order[idx] > now_box:
            now_box += 1
            stack.append(now_box)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx
        
    return idx
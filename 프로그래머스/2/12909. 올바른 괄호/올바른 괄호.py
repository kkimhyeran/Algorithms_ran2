from collections import deque

def solution(s):
    
    q = deque([])
    
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if '(' in q:
                q.remove('(')
            else:
                q.append(i)
    
    if len(q) > 0:
        return False

    return True
def solution(n, m, section):
    
    answer = 0    
    last_painted = 0
    
    for i in section:
        
        if i > last_painted:
            last_painted = i + m -1
            answer += 1

    return answer
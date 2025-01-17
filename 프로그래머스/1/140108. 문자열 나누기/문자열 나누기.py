def solution(s):
    
    answer = 0
    
    x = s[0]
    x_cnt = 1

    not_x_cnt = 0

    for i in range(1, len(s)):
        
        if x_cnt == not_x_cnt:
            answer += 1
            x = s[i]


        if s[i] == x:
            x_cnt += 1
        else:
            not_x_cnt += 1
            
            
    
    return answer + 1
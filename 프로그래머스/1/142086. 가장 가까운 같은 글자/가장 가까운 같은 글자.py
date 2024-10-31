def solution(s):
    
    answer = []
    before_str = ''
    for i in s:
        if i not in before_str:
            answer.append(-1)
            before_str = i + before_str
        else:
            idx = before_str.index(i)
            answer.append(idx+1)
            before_str = i + before_str
                    
        
    
    return answer
def solution(d, budget):
    
    # 1. 부서별 신청 예산 정렬
    d.sort(reverse = False)
    
    # 2. 예산 분배
    answer = 0
    
    for i in d:
        if budget < i:
            break
        
        budget -= i
        answer += 1;
        
    return answer
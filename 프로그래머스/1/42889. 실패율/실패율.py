def solution(N, stages):
    

        
    # 1. 실패율 구하기
    l = len(stages)
    failure_rate = {}
    
    for i in range(1, N+1):
#         challenger_cnt = sum([1 for stage in stages if stage >= i])
#         fail_cnt = sum([1 for stage in stages if stage == i])
        
#         failure_rate[i] = fail_cnt / challenger_cnt
        if l != 0:
            cnt = stages.count(i)
            failure_rate[i] = cnt / l
            l -= cnt
        else:
            failure_rate[i] = 0
    
    # 2. 실패율 내림차순 정렬
    answer = sorted(failure_rate, key=lambda x : failure_rate[x], reverse=True)   
    
    return answer
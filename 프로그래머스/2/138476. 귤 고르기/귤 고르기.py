from collections import Counter

def solution(k, tangerine):
    
    size_cnt = Counter(tangerine) # 각 귤 크기별 빈도 수 구하기
    sorted_size_cnt = sorted(list(size_cnt.values()), reverse=True) # 빈도수 값 정렬

    
    answer = 1
    max_sum = 0
    for i in range(0, len(sorted_size_cnt) - 1):
        
        # size 별 갯수 더하기
        max_sum += sorted_size_cnt[i]
        
        # 만약 k개를 넘어서면 return
        if max_sum >= k:
            return answer
        
        # 귤 사이즈 종류 수 업데이트
        answer += 1
    
    return answer
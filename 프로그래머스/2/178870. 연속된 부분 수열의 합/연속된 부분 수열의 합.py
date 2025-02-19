def solution(sequence, k):
    
    answer = []
    
    n = len(sequence)
    end = 0
    total_sum = 0
    now_len = len(sequence)
    
    for start in range(n):
        
        # 현재 start:end 합이 k에 해당하는 부분 수열 탐색
        while total_sum < k and end < n:
            total_sum += sequence[end]
            end += 1 # 부분 수열 크기 넓히기
            
        if total_sum == k and (end - 1 - start) < now_len:
            answer = [start, end-1] # 가장 최신의 부분 수열 인덱스 정보 업데이트
            # print('현재 부분 수열: {}'.format(sequence[start:end]))
        
        # 최신 수열 길이 업데이트
        now_len = end - 1 - start
        
        # 뒷 수열 탐색
        total_sum -= sequence[start]
                
    return answer
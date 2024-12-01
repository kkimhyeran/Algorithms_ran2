def solution(lottos, win_nums):
    
    ranks = [6, 5, 4, 3, 2, 1, 0]
    answer = []
    
    # 1. 최저 순위
    # 민우 로또 번호에서 win_nums랑 일치하는 개수 구하기
    low_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            low_cnt += 1
    
    
    # 2. 최고 순위
    high_tmp_cnt = 0
    for num in win_nums:
        if num not in lottos:
            high_tmp_cnt += 1
    
    # 최고 순위 개수
    high_cnt = min(lottos.count(0), high_tmp_cnt) + low_cnt
    
    # print(high_cnt)
    if low_cnt < 1:
        low_cnt += 1
    if high_cnt < 1:
        high_cnt += 1
        
    answer.append(ranks.index(high_cnt)+1)
    answer.append(ranks.index(low_cnt)+1)
    
    return answer
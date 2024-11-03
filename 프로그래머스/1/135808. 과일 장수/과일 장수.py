def solution(k, m, score):
    
    # 1. 사과 점수 정렬 + k 이하만
    score.sort(reverse = True)
    
    # 2. 박스에 나눠 담기
    cnt = len(score)//m # 박스 개수
    boxs = []
    for i in range(0, len(score), m):
        boxs.append(score[i:i+m])
    

    # 3. 사과 박스별 점수 계산
    answer = 0
    
    for box in boxs:
        if len(box) >= m:
            answer += min(box)*m
    
        
    return answer
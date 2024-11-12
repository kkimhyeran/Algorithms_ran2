import heapq

def solution(scoville, K):
    # 1. 우선순위 힙에 스코빌 점수 저장
    heapq.heapify(scoville)  # heapq.heappush 대신 heapq.heapify를 사용하여 한 번에 힙을 구성
    
    # 2. 스코빌 지수가 모두 K 이상일 경우
    if scoville[0] >= K:
        return 0
    
    # 3. 섞을 수 없는 경우 (음식이 두 개 미만)
    if len(scoville) < 2:
        return -1
    
    answer = 0
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
    
        answer += 1
        
        if scoville[0] >= K:
            return answer
    
    return -1

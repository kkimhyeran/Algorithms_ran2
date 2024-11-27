def solution(progresses, speeds):

    answer = []
    while progresses:
        for i, progress in enumerate(progresses):
                progresses[i] += speeds[i]
        
        # 배포 가능한 기능 체크
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        # 배포된 기능 개수 추가
        if count > 0:
            answer.append(count)
    
    
    return answer
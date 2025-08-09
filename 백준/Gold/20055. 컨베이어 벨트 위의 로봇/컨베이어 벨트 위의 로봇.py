from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))  # 내구도
robots = deque([False] * N)  # 로봇 위치 (윗부분만 관리)
step = 0

while True:
    step += 1
    
    # 1. 벨트 회전
    belt.rotate(1)
    robots.rotate(1)
    robots[-1] = False  # 내리는 위치 로봇 제거
    
    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):  # 뒤에서부터
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1
    robots[-1] = False  # 내리는 위치 로봇 제거
    
    # 3. 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
    
    # 4. 종료 조건
    if belt.count(0) >= K:
        print(step)
        break

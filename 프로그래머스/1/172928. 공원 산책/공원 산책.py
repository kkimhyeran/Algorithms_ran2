def check_space(x, y, move, park,distance,  disable_space):
    
    n = len(park)
    m = len(park[0])
    
    
    for step in range(1, distance + 1):
        nx = x + move[0] * step
        ny = y + move[1] * step
        
        # 1. 칸 범위 벗어나는지 확인
        if not (0 <= nx < n and 0 <= ny < m):
            return False
        # 2. 장애물 확인
        if [nx, ny] in disable_space:
            return False
    
    return True
    
    
def solution(park, routes):
    
    # 1. 공원 2차열 리스트 생성 + 시작위치 추출
    x, y = 0, 0
    disable_space = []
    
    park_map = []
    for i, row in enumerate(park):
        for j, r in enumerate(row):
            if r == 'S':
                x = i
                y = j
            elif r == 'X':
                disable_space.append([i, j]) # 장애물이 여러개 일 수 있음.
        park_map.append(list(row))
    
    directions = {
        'E': [0, 1],
        'W': [0, -1],
        'N': [-1, 0],
        'S': [1, 0]
    }
    
    # 2. 루트 이동
    for route in routes:
        direction, space = route.split(' ')
        distance = int(space)
        
        move = directions[direction]
        
        if check_space(x, y, move, park, distance, disable_space):
            x += move[0] * distance
            y += move[1] * distance
        
        
    answer = [x, y]
    return answer
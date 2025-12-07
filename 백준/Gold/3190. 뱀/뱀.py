from collections import deque

N = int(input())
K = int(input())

# 보드에 사과 위치 표시
board = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 방향 (오른쪽, 아래, 왼쪽, 위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 처음에는 오른쪽

snake = deque()
snake.append((0, 0))

time = 0
x, y = 0, 0  # 머리 위치

while True:
    time += 1

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽 충돌 체크
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    
    # 자기 몸 충돌 체크
    if (nx, ny) in snake:
        break

    # 머리를 이동
    snake.append((nx, ny))

    # 사과 유무 확인
    if board[nx][ny] == 1:
        board[nx][ny] = 0  # 사과 먹으면 꼬리 그대로
    else:
        snake.popleft()  # 사과 없으면 꼬리 이동

    # 시간에 따른 방향 전환
    if time in turns:
        if turns[time] == 'L':  # 왼쪽
            direction = (direction - 1) % 4
        else:  # D, 오른쪽
            direction = (direction + 1) % 4

    x, y = nx, ny

print(time)
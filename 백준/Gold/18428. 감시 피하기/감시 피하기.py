from itertools import combinations

n = int(input())
board = [input().split() for _ in range(n)]

teachers = []
empties = []

# 선생님 위치, 빈 칸 위치 수집
for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            empties.append((i, j))

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def watch(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] == 'O':  # 장애물
            return False
        if board[nx][ny] == 'S':  # 학생 발견
            return True
        nx += dx
        ny += dy
    return False

def is_safe():
    for x, y in teachers:
        for dx, dy in directions:
            if watch(x, y, dx, dy):
                return False
    return True

answer = "NO"

# 빈 칸 중 3개 선택
for walls in combinations(empties, 3):
    # 장애물 설치
    for x, y in walls:
        board[x][y] = 'O'

    if is_safe():
        answer = "YES"
        break

    # 장애물 제거 (원상 복구)
    for x, y in walls:
        board[x][y] = 'X'

print(answer)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
movement = [list(map(int, input().split())) for _ in range(m)]

# 방향 
direction = {
    1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
    5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)
}

# 초기 구름
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for d, s in movement:
    moved_clouds = set()  # 집합으로 관리

    # 1. 구름 이동 + 비 내리기
    for x, y in clouds:
        nx = (x + s * direction[d][0]) % n
        ny = (y + s * direction[d][1]) % n
        matrix[nx][ny] += 1
        moved_clouds.add((nx, ny))

    # 2. 물복사 버그
    for ci, cj in moved_clouds:
        count = 0
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] > 0:
                count += 1
        matrix[ci][cj] += count

    # 3. 새로운 구름 생성
    clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in moved_clouds and matrix[i][j] >= 2:
                matrix[i][j] -= 2
                clouds.append((i, j))

# 최종 결과
print(sum(map(sum, matrix)))

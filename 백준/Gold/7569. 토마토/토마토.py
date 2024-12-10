from collections import deque
# 1. 입력값
m, n, h = map(int, input().split(' '))

box = [[list(map(int, input().split(' '))) for _ in range(n)] for _ in range(h)]

# print(box)
# 2. 익은 토마토가 있는 위치 뽑기
q = deque([])

visited = [[[False]*m for _ in range(n)] for _ in range(h)]

for x in range(h):
    for y in range(n):
        for z in range(m):
            # print('x: {} y: {} z:{}'.format(x,y,z))
            # 익은 토마토이면
            if box[x][y][z] == 1 and  visited[x][y][z] == False:
                q.append([x,y,z])
                visited[x][y][z] = 1 # 방문 처리

# 3. bfs 탐색
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        # 박스 범위 체크
        if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
            continue

        # 아직 익지 않음 토마토 + 방문하지 않은 칸
        if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
            box[nx][ny][nz] = box[x][y][z] + 1
            visited[nx][ny][nz] = True
            q.append([nx, ny, nz])

# 4. 결과 출력
rslt = 0
for b in box:
    for r in b:
        for c in r:
            if c == 0:
                print(-1)
                exit()
        rslt = max(rslt, max(r))
        
print(rslt-1)
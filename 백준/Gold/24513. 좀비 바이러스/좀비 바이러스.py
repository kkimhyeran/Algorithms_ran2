from collections import deque

n, m = map(int, input().split())
villages = [list(map(int, input().split())) for _ in range(n)]

time = [[-1] * m for _ in range(n)]
q = deque()

# 초기 감염 위치 큐에 등록
for i in range(n):
    for j in range(m):
        if villages[i][j] == 1 or villages[i][j] == 2:
            q.append((i, j, villages[i][j]))  # (x,y,virus)
            time[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x, y, virus = q.popleft()

    # 3번 바이러스는 절대 전파하지 않는다
    if villages[x][y] == 3:
        continue

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if villages[nx][ny] == -1:
                continue

            # 빈 칸이면 감염
            if villages[nx][ny] == 0:
                villages[nx][ny] = virus
                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny, virus))

            # 다른 바이러스가 같은 시간에 도착한 경우  > 혼합 감염 (1번 + 2번)
            elif time[nx][ny] == time[x][y] + 1 and villages[nx][ny] != virus and villages[nx][ny] != 3:
                villages[nx][ny] = 3  # 혼합 확정
                # 3번은 q에 넣지 않는다


# 최종 감염 수 세기
cnt1 = cnt2 = cnt3 = 0
for i in range(n):
    for j in range(m):
        if villages[i][j] == 1:
            cnt1 += 1
        elif villages[i][j] == 2:
            cnt2 += 1
        elif villages[i][j] == 3:
            cnt3 += 1

print(cnt1, cnt2, cnt3)
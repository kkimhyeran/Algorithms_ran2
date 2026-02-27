from collections import deque

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
board = [list(input().strip()) for _ in range(n)]

qs = [deque() for _ in range(p)]
ans = [0] * p

# 초기 성 위치 큐 세팅 + 개수 카운트
for r in range(n):
    for c in range(m):
        ch = board[r][c]
        if ch.isdigit():
            idx = int(ch) - 1
            qs[idx].append((r, c)) # 1번 플레이어가 초기 시작 위치가 2개 이상일 수 있기 때문에
            ans[idx] += 1 # 초기에 차지한 칸 수

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while True:
    progressed = False

    for i in range(p):
        if not qs[i]:
            continue

        max_steps = s[i] # 최대 확장 가능한 칸수
        # i번 플레이어는 이번 턴에 BFS를 max_steps 레벨까지만 수행
        for _ in range(max_steps):
            if not qs[i]:
                break

            layer_size = len(qs[i])
            for _ in range(layer_size):
                r, c = qs[i].popleft()

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == '.':
                        board[nr][nc] = str(i+1)
                        ans[i] += 1
                        qs[i].append((nr, nc))
                        progressed = True

    if not progressed:
        break

print(*ans)
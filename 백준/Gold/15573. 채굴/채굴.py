from collections import deque

def can_mine(D):
    visited = [[False]*(m+2) for _ in range(n+2)]
    q = deque([(0, 0)])
    visited[0][0] = True
    mined = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n+2 and 0 <= ny < m+2):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True

            # 바닥 (nx==n+1) 은 외부 공기가 아니라고 처리
            if nx == 0 or ny == 0 or ny == m+1:
                q.append((nx, ny))
                continue

            if 1 <= nx <= n and 1 <= ny <= m:
                if strength[nx-1][ny-1] <= D:
                    mined += 1
                    if mined >= k:
                        return True
                    q.append((nx, ny))

    return False


n, m, k = map(int, input().split())
strength = [list(map(int, input().split())) for _ in range(n)]

lo, hi = 0, max(max(row) for row in strength)
ans = hi

while lo <= hi:
    mid = (lo + hi) // 2
    if can_mine(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)
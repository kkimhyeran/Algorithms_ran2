from collections import deque
n, k = map(int, input().split())
# n, k = 5, 17

visited = [0] * 100001



def bfs(n, k):

    q = deque()
    q.append(n)

    visited[n] = 1  # 현재 수빈이 위치 방문 처리

    while q:

        now = q.popleft()
        # print(now)

        if now == k:
            return visited[now] - 1

        for i in (now * 2, now - 1, now + 1):
            # 다음 예정된 위치가 범위내에 있고, 아직 방문하지 않았다면
            if (0 <= i <= 100000) and visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1


print(bfs(n, k))
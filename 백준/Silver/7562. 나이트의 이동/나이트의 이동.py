from collections import deque

# 나이트 이동 방향 (총 8가지)
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def dfs():

    q = deque()
    q.append((now_knite[0], now_knite[1]))

    while q:
        x, y = q.popleft() # 현재 방문한 위치 큐에서 출력

        if x == dest_knite[0] and y == dest_knite[1]:
            return chess[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 체스판 안에 있
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny)) # 다음 위치 큐에 저장



t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    
    now_knite = list(map(int, input().split()))
    chess[now_knite[0]][now_knite[1]] = 1
    
    dest_knite = list(map(int, input().split()))
    print(dfs())
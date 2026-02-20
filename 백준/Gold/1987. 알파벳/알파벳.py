from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
boards = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, boards[0][0])) # x, y, 사용한 알파벳 문자열

visited = set()
visited.add((0, 0, boards[0][0]))


ans = 1

while q:
    x, y, path = q.popleft()
    ans = max(ans, len(path))


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if boards[nx][ny] not in path:
                new_path = path + boards[nx][ny]
                state = (nx, ny, new_path)

                if state not in visited:
                    visited.add(state)
                    q.append(state)

print(ans)


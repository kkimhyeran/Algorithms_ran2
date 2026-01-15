students = [list(input().strip()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = set()
princess = set()  # set으로 두면 중복도 자동 제거됨

def dfs(candidate, y_cnt):
    if y_cnt >= 4:
        return

    key = tuple(sorted(candidate))
    if key in visited:
        return
    visited.add(key)

    if len(candidate) == 7:
        princess.add(key)
        return

    for x, y in candidate:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in candidate:
                dfs(candidate + [(nx, ny)], y_cnt + (students[nx][ny] == 'Y'))

for i in range(5):
    for j in range(5):
        if students[i][j] == 'S':
            dfs([(i, j)], 0)

print(len(princess))

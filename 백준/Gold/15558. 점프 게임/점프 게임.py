from collections import deque

n, k = map(int, input().split())
left = list(map(int, input()))
right = list(map(int, input()))

# visited[line][position] 0: 왼쪽, 1: 오른쪽
visited = [[False] * n for _ in range(2)]

q = deque()
q.append((0, 0, 0))  # (줄, 위치, 시간)
visited[0][0] = True

while q:
    line, idx, time = q.popleft()

    # 탈출 조건
    if idx >= n:
        print(1)
        exit()

    # 앞, 뒤, 건너편 + k
    for new_line, new_idx in [(line, idx + 1), (line, idx - 1), (1 - line, idx + k)]:
        if new_idx >= n:
            print(1)
            exit()

        # -1 칸은 없음
        if new_idx < 0:
            continue
        if new_idx <= time:
            continue

        # 이미 방문한 칸이면
        if visited[new_line][new_idx]:
            continue

        # 이동할 수 없는 칸이면
        if (new_line == 0 and left[new_idx] == 0) or (new_line == 1 and right[new_idx] == 0):
            continue

        # 이동했을 경우
        visited[new_line][new_idx] = True # 방문 처리
        q.append((new_line, new_idx, time + 1))

print(0)

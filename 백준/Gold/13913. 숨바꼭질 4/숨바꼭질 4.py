from collections import deque
n, k = map(int, input().split()) # 수빈위치, 동생위치

q = deque([n])

visited = [0] * 100001
previous = [0] * 100001

visited[n] = 1
previous[n] = -1

# 수빈 이동
while q:
    now = q.popleft()

    # 수빈 위치가 동생 위치면 종료
    if now == k:
        break

    # 동생 찾기
    for next in (now*2, now-1, now+1):
        if 0 <= next <= 100000 and visited[next] == 0:
            q.append(next)

            visited[next] = visited[now] + 1
            previous[next] = now # 이전 위치 기록

# 경로 역추적
path_list = []
current = k
while current != -1:
    path_list.append(current)
    current = previous[current]

# 결과 출력
print(visited[k] - 1)
for i in range(len(path_list)-1,-1, -1):
    print(path_list[i])
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# 1. 입력값
n = int(input())

subway_lines = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    subway_lines[a].append(b)
    subway_lines[b].append(a)

# subway_lines = [[], [2, 3], [1, 3], [4, 2, 1, 5], [3, 6], [3], [4]]
cycle_stations = [False] * (n+1)
distance = [-1] * (n + 1)

# 2. 순횐선 여부 확인
def check_cycle(start, now, cnt):
    global is_cycle
    visited[now] = True

    if start == now and cnt >= 2:
        is_cycle = True
        return

    for next in subway_lines[now]:
        if not visited[next]:
            check_cycle(start, next, cnt+1)
        elif next == start and cnt >= 2:
            check_cycle(start, next, cnt)

    return


# 3. 순환선으로 부터 거리 구하기
def get_distance():
    # global distance
    q = deque()

    for i in range(1,n+1):
        # 순환선이면
        if cycle_stations[i] is True:
            distance[i] = 0
            q.append(i)

    while q:
        now = q.popleft()
        for next in subway_lines[now]:
            if distance[next] == -1:
                q.append(next)
                distance[next] = distance[now] + 1


for i in range(1, n+1):
    # 지나온 노드 확인용
    visited = [False for _ in range(n+1)]
    is_cycle = False
    check_cycle(i, i, 0) # 시작, 현재, 개수

    if is_cycle is True:
        cycle_stations[i] = True


get_distance()
# 4. 출력
print(*distance[1:])
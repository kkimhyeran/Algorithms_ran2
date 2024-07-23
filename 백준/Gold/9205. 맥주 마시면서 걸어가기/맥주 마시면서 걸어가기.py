from collections import deque


def bfs():
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if visited[i] == 0:
                new_x, new_y = store_list[i]

                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append(store_list[i])
                    visited[i] = 1

    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    store_list = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    visited = [0 for _ in range(n)]

    bfs()
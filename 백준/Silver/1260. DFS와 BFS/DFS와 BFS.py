'''
@ No: 1260
@ Title: DFS와 BFS
@ key Point: dfs - 스택, 재귀함수 / bfs - 큐


@ 입력값 :
    - n : 정점의 개수
    - m : 간선의 개수
    - v : 탐색을 시작할 정점의 번호

@ 출력값 :
    - dfs 정점 방문 순서
    - bfs 정점방문 순서
'''

from collections import deque

# 1. 압력값
# n = 정점, m = 간점, v = 탐색 시작 정점
n, m, v = map(int, input().split())
# n, m, v = 4, 5, 1

graph = [[0]*n for _ in range(n)]

# 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())

    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

# graph = [[0, 1, 1, 1],
#          [1, 0, 0, 1],
#          [1, 0, 0, 1],
#          [1, 1, 1, 0]]



# 2. dfs
visited_dfs = [0]*n # [0, 0, 0, 0]


# 다 방문할 때 까지 탐색
def dfs(v):
    print(v, end=' ')

    visited_dfs[v-1] = 1

    for i in range(n):
        # 아직 방문하지 않았고
        # 간선이 있다면
        if graph[v-1][i] == 1 and visited_dfs[i] == 0:
            dfs(i+1)

# 3. bfs
visited_bfs = [0] * (n)

def bfs(v):

    will_visit = deque([v-1])
    visited_bfs[v-1] = 1 # 방문처리

    while will_visit:
        v = will_visit.popleft()
        print(v+1, end=' ')

        for i in range(n):
            # v = v + 1
            if graph[v][i] == 1 and visited_bfs[i] == 0:
                # 방문 예정 큐에 추가
                will_visit.append(i)
                visited_bfs[i] = 1





dfs(v)
print()
bfs(v)
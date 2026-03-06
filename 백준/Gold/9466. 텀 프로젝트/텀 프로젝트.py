import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global team_count
    visited[x] = True
    nx = students[x]  # x번 학생이 선택한 학생

    # 다음 학생을 아직 방문하지 않았다면 계속 탐색
    if not visited[nx]:
        dfs(nx)

    # 이미 방문한 학생인데, 아직 DFS가 끝나지 않았다면 사이클
    else:
        if not finished[nx]:
            cur = nx
            team_count += 1

            # 사이클에 포함된 모든 학생 수 세기
            while cur != x:
                cur = students[cur]
                team_count += 1

    # x번 학생에 대한 DFS 종료
    finished[x] = True


t = int(input())

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    team_count = 0

    for i in range(1, n + 1):
        # 아직 탐색하지 않은 학생이면 DFS 시작
        if not visited[i]:
            dfs(i)

    print(n - team_count)
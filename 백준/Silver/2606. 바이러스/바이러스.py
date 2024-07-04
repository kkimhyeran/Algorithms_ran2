
n = int(input())
p = int(input())

pair_list = [[] for _ in range(n+1)] # [[], [], [], [], [], [], [], []]
visited =  [0 for _ in range(n+1)]


# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for _ in range(p):
    num1, num2 = map(int, input().split())
    pair_list[num1].append(num2)
    pair_list[num2].append(num1)

# pair_list = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


def dfs(start):
    stack = [start] # 방문할 노드 번호 스택에 입력
    visited[start] = 1 # 방문 처리
    cnt = 0
    
    while stack:
        node = stack.pop()
        for next in pair_list[node]:
            if visited[next] == 0:
                visited[next] = 1
                stack.append(next)
                cnt += 1
    return cnt

print(dfs(1)) # 1번 노드 부터 시작

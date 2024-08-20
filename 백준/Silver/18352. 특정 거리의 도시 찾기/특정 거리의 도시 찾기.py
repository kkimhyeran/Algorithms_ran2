'''
@ No        : 18352
@ Title     : 특정 거리의 도시 찾기
@ Subject   : 최단거리 - 다익스트라


@ 입력값
    - n : 도시의 개수
    - m : 도로의 개수
    - k : 최단 거리 정보
    - x : 출발 도시 번호
@ 출력값
    - 최단 거리가 k인 도시 정보 출력
'''


import heapq
import sys
f = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, f().split())


graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())

    # a 노드와 연결된 b 노드와 거리
    # graph[1].append((2, 1)) # 1번 노드는 2번 노드와 연결되었으며 거리는 1이다.
    graph[a].append((b, 1))





def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # q에 저장 (0, node)
    distance[start] = 0 # 시작 노드 - 시작 노드 간 거리는 0이다.

    while q:
        # dist : 시작노드에서 현재 노드까지의 거리 총합
        # now : 현재 노드 위치
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드들과의 거리 구하기
        for j in graph[now]:
            cost = dist + j[1] # 현재 노드와 연결된 노드와의 거리 구하기

            # 최단 거리 업데이트
            # 시작 노드와 현재 노드 거리 비교
            # cost: 새로운 거리
            # distance[j[0]]: 기존 거리
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0])) # 다음 탐색 노드 정보 저장

# x는 시작 노드
dijkstra(x)

answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')


from collections import deque

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    importants = list(map(int, input().split()))

    documents = deque()

    for i in range(n):
        documents.append([i, importants[i]])

    cnt = 0

    while documents:
        num, point = documents.popleft()

        if point < max(importants):
            documents.append([num, point])
        else:
            cnt += 1  # 출력이 되었기 때문
            importants[num] = 0

            if num == m:
                print(cnt)
                break

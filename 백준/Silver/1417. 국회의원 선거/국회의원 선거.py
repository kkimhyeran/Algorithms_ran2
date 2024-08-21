import heapq

n = int(input())
candidates = []

dasom = 0
for i in range(n):
    if i == 0:
        dasom = int(input())
    else:
        heapq.heappush(candidates, -int(input()))
    # candidates.append(int(input()))

# n = 5
# candidates = [5, 10, 7, 3, 8]


def get_votes(dasom):
    cnt = 0

    while abs(min(candidates)) >= dasom:
        max_vote = heapq.heappop(candidates)

        if abs(max_vote) >= dasom:
            dasom += 1
            cnt += 1
            heapq.heappush(candidates, max_vote+1)

    return cnt

if n > 1:
    cnt = get_votes(dasom)
else:
    cnt = 0
print(cnt)
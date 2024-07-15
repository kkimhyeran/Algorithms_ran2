# 1. 입력값
n, m = map(int, input().split())
tree_list = list(map(int, input().split()))


# 2. 이진 탐색 범위 정하기
start, end = 1, max(tree_list)


# 3. 절단기 최대 길이 구하기
while start <= end:

    mid = (start + end) // 2

    chk = 0
    for t in tree_list:
        if t > mid:
            chk += (t - mid)

    # 원래 필요한 나무 길이보다 더 길면 절단기 길이를 높인다.
    if chk >= m:
        start = (mid + 1)
    # 필요한 나무 길이보다 작으면 절단기 길이를 낮춘다.
    else:
        end = (mid - 1)


print(end)
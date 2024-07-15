
# 1. 입력값
n = int(input())
budget_list = list(map(int, input().split()))
budget =  int(input())

# 2. 예산 범위
start, end = 1, max(budget_list)

chk = 0
# 3. 예산 배분
while start <= end:
    chk += 1
    mid = (start + end) // 2

    total = 0

    for i in budget_list:
        if i > mid:
            total += mid # 중간값보다 크면 중간값으로
        else:
            total += i # 중간값보다 작으면 해당 예산으로


    if total <= budget:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

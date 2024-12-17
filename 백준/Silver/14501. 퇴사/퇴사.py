# 1. 입력값 받기
n = int(input())

time_tables = [[] for _ in range(n)]
for i in range(n):
    day, pay = map(int, input().split(' '))
    time_tables[i] = [day, pay]

# 2. 각 날짜별 시작일로 하여 금액 계산하기
dp = [0] *  (n + 1)

for i in range(n-1, -1, -1):
    t, p = time_tables[i]

    if i + t <= n:
        dp[i] = max(dp[i + 1], p + dp[i + t])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
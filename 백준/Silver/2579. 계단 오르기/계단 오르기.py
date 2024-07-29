n = int(input())
stair_list = [0]
for _ in range(n):
    stair_list.append(int(input()))

# 각 칸이 마지막 도착 지점일 때 최대 값
if n >= 3:
    dp = [0] * (n + 1)

    # 0번쨰는 계단 오르기 전
    dp[1] = stair_list[1]
    dp[2] = stair_list[1] + stair_list[2]
    dp[3] = max(stair_list[1] + stair_list[3], stair_list[2] + stair_list[3])

    for i in range(4, n+1):
        # 1칸, 2칸 중 최대값
        # 1칸만 올라온 경우 이전에는 무조건 2칸이여야 한다. (3칸 연속으로 오를 수 없기 때문에)
        dp[i] = max(dp[i-3] + stair_list[i-1] + stair_list[i] # 1칸 올라온 경우
                    , dp[i-2] + stair_list[i])                 # 2칸 올라온 경우

    print(dp[n])
else:
    print(sum(stair_list))
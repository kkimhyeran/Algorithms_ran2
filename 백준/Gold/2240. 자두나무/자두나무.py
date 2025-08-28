import sys

input = sys.stdin.readline

# 1. 입력값
t, w = map(int, input().split())
targets = [0] + [int(input()) for i in range(t)]

# 시간 > 행, 이동횟수 > 열
dp = [[0 for _ in range(w+1)] for _ in range(t+1)]
'''
[ [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
, [0, 0, 0]
]
'''

#2. T초 동안 이동 시작
for i in range(1, t+1):


    # 1) 한 번도 이동을 안하는 경우 (즉, 계속 1번 나무에만 있는 거임)
    # 1번 나무에 자두가 떨어지면
    if targets[i] == 1:
        dp[i][0] = dp[i-1][0] + 1

    # 2번 나무에서 자두가 떨어지면 이전에 딴 자두 개수 그대로
    else:
        dp[i][0] = dp[i-1][0]


    # 2) 이동을 한 경우
    for j in range(1, w+1):

        # 1번만 이동한 경우 > 그러면 무조건 2번 나무에 있음 (홀수번 만큼 이동하면)
        if (targets[i] == 2 and j %2 != 0):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        # 2번 이동한 경우 > 그러면 무조건 1번 나무에 있음 (짝수번 만큼만 이동)
        elif (targets[i] == 1 and j %2 == 0):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        # 자두가 떨어지는 나무 <> 현재 나의 위치
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

# 3. 결과 출력
print(max(dp[t]))
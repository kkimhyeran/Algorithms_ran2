import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][0] : 끝점이 (i,j)이고 가로
# dp[i][j][1] : 끝점이 (i,j)이고 세로
# dp[i][j][2] : 끝점이 (i,j)이고 대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 시작 상태
dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):  # 시작 파이프 때문에 2열부터 보면 편함
        
        # 벽이면 지나갈 수 없음
        if board[i][j] == 1:
            continue

        # 가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]

        # 세로
        if i > 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

        # 대각선
        if i > 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))
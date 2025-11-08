N = int(input().strip())
M = int(input().strip())

vip = [int(input().strip()) for _ in range(M)]
    
    
# 피보나치 형태의 dp 테이블
    
dp = [0] * (N + 1) 
dp[0] = 1  
dp[1] = 1

if N >= 2:
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
result = 1
prev = 0
    
# VIP 기준으로 구간 나누기
for v in vip:
    length = v - prev - 1
    result *= dp[length]
    prev = v
    
# 마지막 구간
result *= dp[N - prev]
print(result)
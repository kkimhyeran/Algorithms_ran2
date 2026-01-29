import sys
sys.setrecursionlimit(10**7)

n = int(input().strip())
a, b = map(int, input().split())
m = int(input().strip())
order = [int(input().strip()) for _ in range(m)] # 벽장 여는 순서

def dp(i, x, y):
    if x > y:
        x, y = y, x
    if i == m:
        return 0

    target = order[i] 

    # 1) x 문을 target으로 이동
    cost1 = abs(x - target) + dp(i + 1, target, y) # 옮긴 벽장 위치에서 다시 dp

    # 2) y 문을 target으로 이동
    cost2 = abs(y - target) + dp(i + 1, x, target)

    return min(cost1, cost2) # 이동 거리가 최솟값인 것을 return

print(dp(0, a, b))

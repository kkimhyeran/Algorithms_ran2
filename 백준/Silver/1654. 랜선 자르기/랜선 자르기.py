# 1. 입력값 받기
n, k = map(int, input().split())
lancables = [int(input()) for _ in range(n)]

# 2. 랜선 자를 길이 구하기
start = 1
end = max(lancables)

rslt = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for cable in lancables:
        cnt += cable // mid


    if cnt >= k:
        start = mid + 1
        rslt = mid
    else:
        end = mid -1

print(rslt)


# 1. 입력값
n, c = map(int, input().split())

homes = [int(input()) for _ in range(n)]
homes.sort()

# 2. 이분 탐색
start = 1
end = homes[-1] - homes[0]

while start <= end:

    mid = (start + end) // 2 # 공유기간 최대 거리
    crnt = homes[0] # 현재 위치
    cnt = 1

    for i in range(1, len(homes)):

        if homes[i] >= crnt + mid:
            cnt += 1
            crnt = homes[i]

    if cnt >= c:
        answer = mid
        start = mid + 1
    
    # 설치하고자 하는 공유기 수보다 작을 경우 최대 거리 줄이기
    else:
        end = mid - 1

print(answer)

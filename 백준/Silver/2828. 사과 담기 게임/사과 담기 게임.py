
# 1. 입력값
n, m = map(int, input().split())
j = int(input()) # 사과 개수

apple_positions = [int(input()) for _ in range(j)]

# 2. 바구니 위치 + 칸수 범위 변수 설정
bucket_start = 1
bucket_end = m # 바구니 칸수

# 3.사과 담기 게임
dist = 0
for now in apple_positions:
    # 1. 바구니 위치 <= 현재 사과 위치 <= 칸 수
    if bucket_start <= now <= bucket_end :
        continue
    # 2. 현재 위치 > 사과 떨어지는 위치
    elif now < bucket_start:
        dist += (bucket_start - now)
        bucket_end -= (bucket_start - now)
        bucket_start = now

    # 3. 현재 위치 < 사과 떨어지는 위치
    else:
        dist += (now - bucket_end)
        bucket_start += (now - bucket_end)
        bucket_end = now


print(dist)
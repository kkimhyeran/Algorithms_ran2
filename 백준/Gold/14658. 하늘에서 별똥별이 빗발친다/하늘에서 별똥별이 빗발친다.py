# 1. 입력값
n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]

max_hit = 0

# 2. 모든 별똥별의 위치를 기준으로 트램펄린 왼쪽 아래 모서리를 잡고 검사
for i in range(k):
    for j in range(k):
        sx = stars[i][0]
        sy = stars[j][1]

        # 트램펄린이 (sx, sy)를 왼쪽 아래 모서리로 커버하는 범위 내 별 개수 세기
        cnt = 0
        for x, y in stars:
            if sx <= x <= sx + l and sy <= y <= sy + l:
                cnt += 1

        # 튕겨낸 별똥별 갯수 업데이트
        max_hit = max(max_hit, cnt)

print(k - max_hit)

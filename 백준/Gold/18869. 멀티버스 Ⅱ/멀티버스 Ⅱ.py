from itertools import combinations
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

# 우주 행성 크기 정보 입력
planets = []
for _ in range(m):
    planets.append(list(map(int, input().split())))

# 각 우주를 순위 패턴으로 변환
patterns = []

for planet in planets:
    # 값 정렬 후 순위 매기기
    sorted_unique = sorted(set(planet))
    rank = {value: idx for idx, value in enumerate(sorted_unique)} # 행성 크기 : 크기 순위

    # 원래 순서를 유지한 채 순위로 변환
    # [1, 3, 2] > (0, 2, 1)
    pattern = tuple(rank[value] for value in planet) # 각 행성 크기별 순위 구하기
    patterns.append(pattern)

# 같은 패턴을 가진 우주의 쌍 개수 세기
cnt = 0
for a, b in combinations(patterns, 2):
    if a == b:
        cnt += 1

print(cnt)
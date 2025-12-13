n = int(input())
villages = []

for _ in range(n):
    x, a = map(int, input().split())
    villages.append((x, a))

# 위치 기준 정렬
villages.sort()

total_population = sum(a for _, a in villages)
half = (total_population + 1) // 2  # 중앙 기준

current = 0
for x, a in villages:
    current += a
    if current >= half:
        print(x)
        break
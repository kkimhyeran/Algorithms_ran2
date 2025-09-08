# 1. 입력값

n = int(input())
liquid_list = list(map(int, input().split()))

# 2. 범위를 좁혀가면 탐색?

start = 0
end = n - 1

target_total_sum = float('INF')

while start < end:
    # 현재 혼합용액 특성값
    curr_total_sum = liquid_list[start] + liquid_list[end]

    if abs(curr_total_sum) < abs(target_total_sum):
        target_total_sum = curr_total_sum # 목표값 갱신
        result = [liquid_list[start], liquid_list[end]]

    if curr_total_sum < 0:
        start += 1

    else:
        end -= 1

print(result[0], result[1])



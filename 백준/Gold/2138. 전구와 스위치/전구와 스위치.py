n = int(input().strip())
now = list(map(int, list(input().strip())))
target = list(map(int, list(input().strip())))

def switch_bulbs(state, target, press_first):
    n = len(state)
    bulbs = state[:]  # 복사
    cnt = 0

    # 첫 번째 스위치 누를 경우 처리
    if press_first:
        cnt += 1
        bulbs[0] = 1 - bulbs[0]
        bulbs[1] = 1 - bulbs[1]

    # 2번 스위치부터 N번까지
    for i in range(1, n):
        if bulbs[i - 1] != target[i - 1]:
            cnt += 1
            bulbs[i - 1] = 1 - bulbs[i - 1]
            bulbs[i] = 1 - bulbs[i]
            if i + 1 < n:
                bulbs[i + 1] = 1 - bulbs[i + 1]

    # 마지막 확인
    if bulbs == target:
        return cnt
    else:
        return float('inf')

# 2. 스위치 버튼
res1 = switch_bulbs(now, target, False)  # 1번 스위치 안 누름
res2 = switch_bulbs(now, target, True)   # 1번 스위치 누름

ans = min(res1, res2)
print(ans if ans != float('inf') else -1)

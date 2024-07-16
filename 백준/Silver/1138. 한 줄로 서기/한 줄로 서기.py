
n = int(input())
info_list = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    chk = 0
    for j in range(n):
        # 앞에 키큰 사람 수 확인 + 현재 자리가 비어있는 경우
        if chk == info_list[i] and result[j] == 0:
            result[j] = i+1
            break
        elif result[j] == 0:
            chk += 1


print(*result)
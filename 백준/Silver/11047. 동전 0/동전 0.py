n, k = map(int, input().split(' '))

# 동전의 종류를 동전의 개수 n만큼 입력 받음
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

cnt = 0
for coin in coin_list:
    if k / coin >= 1:

        cash_cnt = k // coin
        k -= coin * cash_cnt
        cnt += cash_cnt

print(cnt)
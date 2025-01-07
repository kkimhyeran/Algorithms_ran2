# 1. 입력값
k = int(input())

# 2. k 이상의 초콜릿 크기
n = 0
while True:
    if 2**n >= k:
        break
    n += 1

count = 0
size = 2**n

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(2**n, count)
import sys
input = sys.stdin.readline

# 1. 입력값
n = int(input())
loaf_list = [int(input()) for _ in range(n)]

# 2. 로프 내림차순 정렬
loaf_list.sort(reverse=True)

# 3. 최대 중랼 구하기
result = []
for i in range(n):
    result.append(loaf_list[i]*(i+1))

print(max(result))
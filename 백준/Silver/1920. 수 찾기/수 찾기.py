
# 1. 입력값
n = int(input())
num_list = set(map(int, input().split()))

m = int(input())
chk_list = list(map(int, input().split()))


# 2. 존재여부 확인
# 존재하면 1 , 아니면 0 출력
[print(1) if i in num_list else print(0) for i in chk_list]


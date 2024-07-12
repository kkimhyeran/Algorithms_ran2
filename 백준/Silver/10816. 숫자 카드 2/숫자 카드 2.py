# 1. 입력값
n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
chk_list = list(map(int, input().split()))


num_dict = {}
for num in num_list:
    if num in num_dict.keys():
        num_dict[num] = num_dict[num] + 1
    else:
        num_dict[num] = 1


for val in chk_list:
    if val in num_dict.keys():
        print(num_dict[val], end= ' ')
    else:
        print(0, end=' ')
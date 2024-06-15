# 1. 입력값
n = int(input())

cows_location_list = []
for _ in range(n):
    cow, location = map(int, input().split(' '))
    cows_location_list.append([cow, location])

# 2. 소 이동 횟수 세기
# 일단 최초 입력되는 소들은 cow_dict에 저장
# 최초 입력이 아닌 소들 중 마지막 위치 값과 다른 경우에 소 이동 횟수를 증가한다.

move_cnt = 0

cow_dict = {}
for cow, location in cows_location_list:
    if cow not in cow_dict:
        cow_dict[cow] = [location]
    elif cow in cow_dict and (cow_dict[cow][-1] != location):
        cow_dict[cow] = [location]
        move_cnt += 1

print(move_cnt)

# 1. 입력값

# 1) 철수 빙고
bingo_matrix = []
for i in range(5):
     bingo_matrix.append(list(map(int, input().split())))


# 2) 사회자가 부를 값
number_list = []
for i in range(5):
     number_list.extend(list(map(int, input().split())))

cnt = 0

# 2. 빙고 맞추기
for number in number_list:

    for x in range(len(bingo_matrix)):
        for y in range(len(bingo_matrix[0])):

            if number == bingo_matrix[x][y]:
                bingo_matrix[x][y] = 0

    # 3. 빙고 줄 확인하기
    # 3-1) 새로 줄 확인
    for i in list(zip(*bingo_matrix)):
        if sum(list(i)) == 0:
            cnt += 1

    for j in bingo_matrix:
        if sum(j) == 0:
            cnt += 1

    left_side = 0
    right_side = 0
    for k in range(len(bingo_matrix)):
        left_side += bingo_matrix[k][k]
        right_side += bingo_matrix[k][len(bingo_matrix)-1-k]

    if left_side == 0:
        cnt += 1
    if right_side == 0:
        cnt += 1


    if cnt >= 3:
        print(number_list.index(number)+1)
        break
    else:
        cnt = 0

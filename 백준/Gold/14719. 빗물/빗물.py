'''
@ No        : 14719
@ Title     : 빗물
@ Subject   : 구현

@ 입력값
    - h, w : 세로, 세로 길이
    - rain_h : 빗물의 높이
@ 출력값
    - rain_amount : 고인 빗물 총 용량
'''




h, w = map(int, input().split())
block_height_list = list(map(int, input().split()))


rain_block = [[0]*w for i in range(h)]




for i in range(w):
    for j in range(h-block_height_list[i],h):
        # print('rain_block[{}][{}]'.format(j,i))
        rain_block[j][i] = 1

# 블록 밑에서 부터 확인
for row in range(h-1, -1, -1):
    # print(row)
    for col in range(w):
        # 현재 블록이 채워져 있지 않으면
        if rain_block[row][col] == 0 and col != 0:
            # 앞 블록이 있어야 하고 뒷 블록 1이 나올 때 까지 확인 한 후에
            until_block_colnum = -1
            if rain_block[row][col-1] == 1:
                # 빈 칸부터 블록이 채워진 칸까지 확인하고
                # 만약 채워진 칸이 있으면
                for sub_col in range(col+1, w):
                    if rain_block[row][sub_col] == 1:
                        until_block_colnum = sub_col
                        break

            if until_block_colnum != -1:
                # 물이 고이는 곳은 2로 채움
                for accum_col in range(col, until_block_colnum):
                    rain_block[row][accum_col] = 2




print(sum(rain_block, []).count(2))





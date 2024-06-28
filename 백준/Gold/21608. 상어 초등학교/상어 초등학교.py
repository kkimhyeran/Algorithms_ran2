'''
@ No        : 21608
@ Title     : 상어 초등학교
@ Subject   : 구현

@ 입력값:
    - n : n^2 = 교실의 크기, 학생들의 수
@ 출력값
    - 학생들 만족도 총 합
'''


import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 1. 입력값 받기
n = int(input())
bestfreinds_list =  [list(map(int, input().split())) for _ in range(n**2)]


# 학생들이 앉을 빈자리 배열
sit_list = [[0]*n for i in range(n)]


for student in bestfreinds_list:
    # print(student)
    # 학생 순서대로 각 자리를 돌면서 우선 순위를 매긴 뒤에 자리 선정

    # 해당 학생이 앉을 수 있는 자리 저장
    sit_able_list = []

    for i in range(len(sit_list)):
        for j in range(len(sit_list[0])):

            # 빈 자리이면
            if sit_list[i][j] == 0:
                favorite = 0
                blank = 0

                # 인접한 칸들 확인
                for b in range(4):
                    nx = i + dx[b]
                    ny = j + dy[b]

                    # 교실을 넘어선 자리는 제외
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    # 친구 확인 > 인접한 칸에 친구가 존재하면 +1
                    if sit_list[nx][ny] in student[1:]:
                        favorite += 1
                    # 인접한 칸이 빈자리면 +1
                    if sit_list[nx][ny] == 0:
                        blank += 1

                # 자리 우선 순위 정렬시 쉽게 보기위한 입력 순서
                # 친구 > 인접한 칸의 빈자리 개수 > 행 작은값 > 열 작은 값
                sit_able_list.append([favorite, blank, i, j])

    # 자리 우선순위: 친구 많은 > 인접한 칸의 빈자리 개수가 많은 > 행 작은값 > 열 작은 값
    sit_able_list.sort(key = lambda x:(-x[0],-x[1], x[2], [3]))
    sit_list[sit_able_list[0][2]][sit_able_list[0][3]] = student[0]


# 만족도 구하기
# 각 자리별로 좋아하는 친구 수 세기
answer = 0
score = [0, 1, 10, 100, 1000]
bestfreinds_list.sort() # 학생 번호대로 오름차순 정렬

for i in range(n):
    for j in range(n):

        # 현재 만족도를 구하는 학생
        # student = sit_list[i][j]
        cnt = 0

        # 인접한 칸에 있는 친구 추출
        for b in range(4):
            nx = i + dx[b]
            ny = j + dy[b]

            # 교실을 넘어선 자리는 제외
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 해당 인접 칸에 있는 친구가 내가 좋아하는 친구이면 students[data[i][j] - 1]
            if sit_list[nx][ny] in bestfreinds_list[sit_list[i][j] - 1][1:]:
                cnt += 1

        answer += score[cnt]

# 만족도 총합
print(answer)


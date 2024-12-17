# 1. 입력값
r, c, t = map(int, input().split(' '))

matrix = [list(map(int, input().split())) for _ in range(r)]



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

air_cleaner = []
for x in range(r):
    for y in range(c):
        if matrix[x][y] == -1:
            air_cleaner.append(x)  # 공기청정기 위치 찾기
def spread():
    # 2. 미세먼지 확산
    # 기존에 미세먼지가 있는 칸인지 여부
    tmp_matrix = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):

            # 미세먼지가 있는 칸이면
            if matrix[x][y] > 4:
                # 퍼지는 미세먼지 양
                amount = matrix[x][y] // 5

                # 퍼지는 미세먼지 칸
                cnt = 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 범위가 벗어나지 않는지 확인
                    if 0 <= nx < r and 0 <= ny < c:
                        # 공기 청정기 칸만 아니면 퍼질 수 있다.
                        if matrix[nx][ny] != -1:
                            # 다른 칸에서 영향받은 미세먼지 양까지 더해야 하므로
                            # 현재 퍼진 양 + 퍼시는 미세먼지 양
                            tmp_matrix[nx][ny] += amount
                            tmp_matrix[x][y] -= amount

    for x in range(r):
        for y in range(c):
            matrix[x][y] += tmp_matrix[x][y]
         
def clean_air():
    # 시게방향
    for i in range(air_cleaner[1] + 1, r - 1):
        matrix[i][0] = matrix[i + 1][0]
    for i in range(c - 1):
        matrix[r - 1][i] = matrix[r - 1][i + 1]
    for i in range(r - 1, air_cleaner[1], -1):
        matrix[i][c - 1] = matrix[i - 1][c - 1]
    for i in range(c - 1, 0, -1):
        if matrix[air_cleaner[1]][i - 1] == -1:
            matrix[air_cleaner[1]][i] = 0
        else:
            matrix[air_cleaner[1]][i] = matrix[air_cleaner[1]][i - 1]

    # 반시계 방향
    for j in range(air_cleaner[0] - 1, 0, -1):
        matrix[j][0] = matrix[j - 1][0]
    for j in range(c - 1):
        matrix[0][j] = matrix[0][j + 1]
    for j in range(air_cleaner[0]):
        matrix[j][c - 1] = matrix[j + 1][c - 1]
    for j in range(c - 1, 0, -1):
        if matrix[air_cleaner[0]][j - 1] == -1:
            matrix[air_cleaner[0]][j] = 0
        else:
            matrix[air_cleaner[0]][j] = matrix[air_cleaner[0]][j - 1]
# t초 만큼 반복
for _ in range(t):

    spread()
    clean_air()


# 3. 미세먼지 총량 구하기
result = 0
for row in matrix:
    result += sum(row)
print(result + 2)
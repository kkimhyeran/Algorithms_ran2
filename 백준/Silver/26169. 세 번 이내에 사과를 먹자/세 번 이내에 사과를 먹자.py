# 1. 입력값
# 1: 사과, -1: 장애물, 0: 빈칸

boards = []
for _ in range(5):
    temp = list(map(int, input().split()))
    boards.append(temp)


x, y = map(int, input().split())

# 2. dfs + 백트래킹
chk = False

def dfs(x, y, move, cnt):
    global chk

    if x > 4 or y > 4 or x < 0 or y < 0 or move > 3:
        return

    # 장애물
    if boards[x][y] == -1:
        return

    # 사과
    if boards[x][y] == 1:
        cnt += 1

    # 빈칸
    # 백트래킹
    tmp = boards[x][y]
    boards[x][y] = -1 # 방문처리

    # 먹은 사과 개수가 2개 이상이면 나가기
    if cnt == 2:
        chk = True
        return

    dfs(x + 1, y, move + 1, cnt)
    dfs(x - 1, y, move + 1, cnt)
    dfs(x, y + 1, move + 1, cnt)
    dfs(x, y - 1, move + 1, cnt)

    boards[x][y] = tmp # 갔던 길에서 막히면 원래 값으로 원복


dfs(x, y, 0, 0)

# 3. 출력
if chk:
    print(1)
else:
    print(0)


# https://zzzini-5.tistory.com/222?
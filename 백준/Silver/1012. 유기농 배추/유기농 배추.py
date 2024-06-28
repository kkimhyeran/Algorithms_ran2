# 배추지렁이 수 구하기
import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    # print('{}, {} 위치의 배추를 확인하고 있습니다.'.format(x, y))
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if bachu[x][y] == 1:
        bachu[x][y] = 0

        # 상,하, 좌, 우 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    else:
        return False

# 1. 입력값 받기
# t: 테스트 개수
test_cnt = int(input())
test_rlt = []

for t in range(test_cnt):
    # 배추밭 크기(m = 가로, n = 세로), 배추 개수
    m, n, k = map(int, input().split())

    # 테스트 케이스 만큼 배추밭 크기, 배추가 심어진 개수, 각 배추 위치값 입력 받기

    # 일단 전체 배추밭에 심어진 배추가 없다고 하자.
    bachu = [[0]*n for i in range(m)]

    # 배추가 있는 위치값 입력 받을 때 마다 업데이트
    for j in range(k):
        # x = 행, y = 열
        x, y = map(int, input().split())
        bachu[x][y] = 1


    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1

    test_rlt.append(result)



for rlt in test_rlt:
    print(rlt, end =' ')





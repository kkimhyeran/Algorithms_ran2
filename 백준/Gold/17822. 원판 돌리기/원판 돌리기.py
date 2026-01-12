import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력값
n, m, t = map(int, input().split())

circle_dict = {}
for i in range(1, n + 1):
    circle_dict[i] = deque(map(int, input().split()))  # 회전 편하게 deque로

rotations = [list(map(int, input().split())) for _ in range(t)]


def rotate_disk(dq: deque, d: int, k: int) -> None:

    # 0: 시계, 1: 반시계
    k %= m
    if k == 0: # 움직이는 칸이 = 0
        return

    if d == 0:
        dq.rotate(k)      # 시계 방향: 오른쪽으로 k
    else:
        dq.rotate(-k)     # 반시계: 왼쪽으로 k


# 2. T번 시뮬레이션
for _ in range(t):
    x, d, k = rotations[_]

    # 2-1) x의 배수인 원판들 회전
    for disk_num in range(x, n + 1, x):
        rotate_disk(circle_dict[disk_num], d, k)

    # 3) 인접한 칸 (상하좌우)에 같은 수 있는지 확인해서 지울 값 위치 저장
    to_remove = set()

    # 원판을 2차원처럼 보고 검사
    for i in range(1, n + 1):

        # m개의 정수 검사
        for j in range(m):
            cur = circle_dict[i][j]

            if cur == 0:
                continue

            # 좌우
            left_j = (j - 1) % m
            right_j = (j + 1) % m

            if circle_dict[i][left_j] == cur:
                to_remove.add((i, j))
                to_remove.add((i, left_j))
            if circle_dict[i][right_j] == cur:
                to_remove.add((i, j))
                to_remove.add((i, right_j))

            # 상하
            if i > 1 and circle_dict[i - 1][j] == cur:
                to_remove.add((i, j))
                to_remove.add((i - 1, j))
            if i < n and circle_dict[i + 1][j] == cur:
                to_remove.add((i, j))
                to_remove.add((i + 1, j))

    # 3-1) 지울 게 있으면 0으로
    if to_remove:
        for (i, j) in to_remove:
            circle_dict[i][j] = 0

    # 3-2) 지울 게 없으면 원판 평균으로 조정
    else:
        total = 0
        cnt = 0

        for i in range(1, n + 1):
            for v in circle_dict[i]:
                if v != 0:
                    total += v
                    cnt += 1

        # 남은 수가 하나도 없으면 그냥 전부다 0임
        if cnt == 0:
            continue

        # 해당 원판 평균 구하기
        avg = total / cnt

        for i in range(1, n + 1):
            for j in range(m):
                v = circle_dict[i][j]
                if v == 0:
                    continue

                if v > avg:
                    circle_dict[i][j] = v - 1 # 평균보다  큰 수는 -1
                elif v < avg:
                    circle_dict[i][j] = v + 1 # 평균보다 작은 수는 +1


# 4. 최종 합 출력
ans = 0
for i in range(1, n + 1):
    ans += sum(circle_dict[i])

print(ans)

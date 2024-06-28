from copy import deepcopy


t = int(input())
for _ in range(t):
    n, rotate = map(int, input().split())
    # n = 5
    # rotate = 135
    org_array = [list(map(int, input().split())) for _ in range(n)]

    # 결과 저장할 배열
    result = [[0] * n for _ in range(n)]

    if rotate < 0:
        rotate = 360 + rotate

    # 회전이 없는 경우
    # 굳이 회저
    if rotate == 360 or rotate == 0:
        for i in org_array:
            print(*i)

    
    else:
        # rotate // 45 수 많큼 배열을 회전한다.
        # 즉, 90도 이면 2번 회전해서
        # 주 대각선 > 가운데 열 > 가운데 행으로 이동 > 즉, 최종적으로 옮겨야 하는 위치로 이동한다.
        for _ in range(rotate // 45):
            for i in range(4):
                # 주 대각선 > 가운데 열
                if i == 0:
                    for j in range(n):
                        result[j][n//2] = org_array[j][j]
                # 가운데 열 > 부 대각선
                elif i == 1:
                    for j in range(n):
                        result[j][n-1-j] = org_array[j][n//2]
    
                # 부 대각선 > 가운데 행
                elif i == 2:
                    for j in range(n):
                        result[n//2][j] = org_array[n-1-j][j]
    
                # 가운데 행 > 주 대각선
                elif i == 3:
                    for j in range(n):
                        result[j][j] = org_array[n//2][j]
    
            for i in range(n):
                for j in range(n):
                    if result[i][j] == 0:
                        result[i][j] = org_array[i][j]
    
            # 다시 회전해야 할 수도 있으니 업데이트
            org_array = deepcopy(result)
    
        for i in result:
            print(*i)
    
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    # 1. 입력값 받기
    k = int(input())
    n = int(input())

    # 2. 입력받은 k층 n호 사는 사람 수 구하기
    living_peoples = [[] for _ in range(k+1)]
    for i in range(0, k+1):
        for j in range(1, n+1):
            if i != 0:
                living_peoples[i].append(sum(living_peoples[i-1][:j]))
            else:
                living_peoples[i].append(j)

    # 3. 결과 출력
    print(living_peoples[k][n-1])
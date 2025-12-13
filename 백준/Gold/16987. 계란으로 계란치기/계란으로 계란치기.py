import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
s = []
w = []
for _ in range(n):
    si, wi = map(int, sys.stdin.readline().split())
    s.append(si)
    w.append(wi)

ans = 0

def dfs(i):
    global ans

    # 끝까지 들었으면 깨진 개수 갱신
    if i == n:
        broken = 0
        for k in range(n):
            if s[k] <= 0:
                broken += 1
        ans = max(ans, broken)
        return

    # 현재 들 계란이 이미 깨져 있으면 넘어감
    if s[i] <= 0:
        dfs(i + 1)
        return

    # 안 깨진 다른 계란 찾기
    has_target = False
    for j in range(n):
        if j == i:
            continue
        if s[j] > 0:
            has_target = True

            # i로 j를 침: 서로 내구도 감소
            si_before = s[i]
            sj_before = s[j]

            s[i] -= w[j]
            s[j] -= w[i]

            dfs(i + 1)

            # 원상복구
            s[i] = si_before
            s[j] = sj_before

    # 칠 대상이 없으면 그냥 넘어감
    if not has_target:
        dfs(i + 1)

dfs(0)
print(ans)
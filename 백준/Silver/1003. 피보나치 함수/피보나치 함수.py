
t = int(input())
for _ in range(t):
    n = int(input())

    cnt0, cnt1 = 1, 0
    for _ in range(n):
        cnt0, cnt1 = cnt1, cnt0 + cnt1
    print(cnt0,cnt1)

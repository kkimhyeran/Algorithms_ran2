n = int(input())
work_list = [list(map(int, input().split())) for _ in range(n)]

work_list = sorted(work_list, key = lambda x: (x[1], x[0]), reverse = True)


time = work_list[0][1]

for i in range(n):

    if work_list[i][1] <= time:
        # 다음 작업 end_time
        time = (work_list[i][1] - work_list[i][0])

    else:
        time -= work_list[i][0]
        
if time >= 0:
    print(time)
else:
    print(-1)
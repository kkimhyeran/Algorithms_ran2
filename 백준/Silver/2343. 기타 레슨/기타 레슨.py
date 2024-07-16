# 1. 입력값
n, m = map(int, input().split())
lecture_list = list(map(int, input().split()))

# 2. 블루레이 크기 범위
start, end = max(lecture_list), sum(lecture_list)


while start <= end:

    mid = (start + end) // 2

    cnt = 1 # 우선 첫번째 블루레이에 강의 배분
    time = 0

    for i in lecture_list:

        if time + i > mid:
            cnt += 1 # 다음 블루레이로 넘어간다.
            time = 0 # 시간 초기화

        time += i


    if cnt <= m:
        end = mid - 1
        rslt = mid
    else:
        start = mid + 1

print(rslt)
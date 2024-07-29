
n = int(input())
sequence_list = list(map(int, input().split()))

# dp: 각 인덱스 요소가 수열의 마지막 일 때 길이 저장
dp = [1] * n

# i: 부분 수열 마지막 인덱스 번호
for i in range(1, n):

    # j ~ i 까지 부분 수열 길이 구하기
    for j in range(i):
        if sequence_list[j] < sequence_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)



print(max(dp))

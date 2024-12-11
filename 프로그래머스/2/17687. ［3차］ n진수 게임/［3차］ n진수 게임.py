def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t):
        result = ""
        while num > 0:
            num, remainder = divmod(num, n)
            result += notation[remainder]

        answer += result[::-1] # 추출한 n진수로 바꾸기 위해 뒤집기
    
    # answer[p-1::m]: p-1 인덱스 부터 m 간격으로 슬라이싱
    # answer[p-1::m][:t] : t개 값만 추출
    return answer[p-1::m][:t]

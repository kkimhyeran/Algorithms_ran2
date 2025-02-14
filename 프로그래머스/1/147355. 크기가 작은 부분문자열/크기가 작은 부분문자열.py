def solution(t, p):
    
    # 1. p 길이만큼 숫자 구학
    numbers = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    
    # 2. p보다 같거나 작은 구 수하기
    int_p = int(p)
    answer = sum([1 for num in numbers if num <= int_p])
    # answer = 0
    return answer
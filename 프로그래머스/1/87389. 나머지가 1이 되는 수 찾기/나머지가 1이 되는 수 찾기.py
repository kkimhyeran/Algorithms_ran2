def solution(n):
    
    # 1. 최소 공약수 구하기
    numbers = []
    for i in range(1, n):
        if (n-1) % i == 0 and i != 1:
            numbers.append(i)
            
    numbers.sort()
    # answer = 0
    return numbers[0]
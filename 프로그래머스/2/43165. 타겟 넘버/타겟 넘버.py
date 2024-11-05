answer = 0

def dfs(i, total_sum, numbers, target):
    global answer
    
    # 만약 마지막 계산 도착 + 결과가 target이면
    if i == len(numbers):
        if total_sum == target:
            answer += 1
        return
    
    else:
        dfs(i+1, total_sum + numbers[i], numbers, target) # 덧셈
        dfs(i+1, total_sum - numbers[i], numbers, target) # 뺄셈

    
def solution(numbers, target):
    
    i = 0
    total_sum = 0
    dfs(i, total_sum, numbers, target)
    

    return answer
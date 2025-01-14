def solution(numbers):
    
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            print('{} + {} = {}'.format(numbers[i], numbers[j],numbers[i]+numbers[j] ))
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer = sorted(answer)
    return answer
def solution(people, limit):
    # 1. people 내림차순 정렬
    people.sort()
    
    # 2. 배 태우기
    start = 0
    end = len(people) - 1
    answer = 0
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        
    
            
    return answer
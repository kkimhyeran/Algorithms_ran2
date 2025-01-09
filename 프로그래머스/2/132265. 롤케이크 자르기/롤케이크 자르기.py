from collections import Counter
def solution(topping):
    
    answer = 0
    older = Counter(topping) 
    younger = set()
    
    # 철수가 모든 토핑을 가진 상태에서 동생에게 하나씩 준다.
    for i in topping:
        
        # 철수 > 동생 토핑 1개 주기
        older[i] -= 1
        younger.add(i)
        
        if older[i] == 0:
            older.pop(i)
            
        if len(older) == len(younger):
            answer += 1
    return answer
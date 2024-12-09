
def solution(n, m):
    
    # 1. 최대공약수
    common1_numbers = []
    for i in range(1, n+1):
        if n % i == 0 and i not in common1_numbers:
            common1_numbers.append(i)
    
    common2_numbers = []
    for i in range(1, m+1):
        if m % i == 0 and i not in common2_numbers:
            common2_numbers.append(i)
    

    common_numbers = list(set(common1_numbers).intersection(set(common2_numbers)))
    
    
    # 최소공배수
    minimum_number =  (n*m) / max(common_numbers) 
        
            
    answer = [max(common_numbers) , minimum_number]
    return answer
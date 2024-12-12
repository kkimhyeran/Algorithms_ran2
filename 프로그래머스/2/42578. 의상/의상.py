from itertools import combinations

def solution(clothes):
    
    # 1. clothes dict
    clothes_dict = {}
    for cloth in clothes:
        value, key = cloth

        if key in clothes_dict.keys():
            clothes_dict[key] += 1
        else:
            clothes_dict[key] = 1
            
    
    answer = 1
    # 개수 구하기
    for val in clothes_dict.values():
        answer *= val + 1
        
    
    return answer - 1
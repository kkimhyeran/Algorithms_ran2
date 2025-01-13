from collections import Counter
def solution(want, number, discount):
    
    # 1. 각 품목별 구매해야할 갯수
    product_dict = {want[i]:number[i] for i in range(len(want))}
    
    # 2. 할인 시작 날짜별로 품목 충족 여부 확인
    answer = 0
    for i in range(len(discount)-sum(number)+1):
        if product_dict == Counter(discount[i:i+10]):
            answer +=1

        # print(product_dict)
        # print(Counter(discount[i:i+10]))
        # print()
    return answer
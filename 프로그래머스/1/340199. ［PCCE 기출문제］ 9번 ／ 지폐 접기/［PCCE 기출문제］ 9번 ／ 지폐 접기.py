def solution(wallet, bill):
    
    # 지갑 가로, 세로 길이
    wallet_min = min(wallet)
    wallet_max = max(wallet)
    
    # 지폐 가로, 세로 길이
    bill_min = min(bill)
    bill_max = max(bill)
    
    # 지폐 접기
    answer = 0
    while (wallet_min < bill_min or wallet_max < bill_max):
        print('최대값:{}'.format(bill_max))
        print('최소값:{}\n'.format(bill_min))
        
        if bill_max > bill_min:
            bill_max = bill_max // 2
        else:
            bill_min = bill_min // 2
        answer += 1
        
        if bill_min > bill_max:
            tmp = bill_min
            bill_min = bill_max
            bill_max = tmp
    
    return answer
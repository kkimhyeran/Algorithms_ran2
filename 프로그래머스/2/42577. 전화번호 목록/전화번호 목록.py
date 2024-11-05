def solution(phone_book):
    
    # 1. 번호 dict 생성
    phonebook_dict = {nums:1 for nums in phone_book}
    
    
    # 2. 접두어 찾기
    answer = True
    
    for number in phone_book:
        prefix = "" 
        
        for num in number: 
            prefix += num
            
            if prefix in phonebook_dict.keys() and prefix != number:       
                return False 
    
    return answer
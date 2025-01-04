def binary_number(number):
    num = ''
    while number:
        number, quot = divmod(number, 2)
        num += str(quot)
    return num[::-1]

def solution(s):
    
    binary_cnt = 0
    remove_zero = 0
    while s != '1':
        # 1. 모든 0 제거하기
        remove_zero += s.count('0')
        s = s.replace('0', '')
        
        # 2. s의 길이 값을 2진법으로 표현.
        s = binary_number(len(s))
        
        binary_cnt += 1
    
    answer = [binary_cnt, remove_zero]
    return answer
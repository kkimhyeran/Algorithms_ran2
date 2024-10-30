# 소수 판단하는 함수
def is_prime_number(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    
    for i in range(2, int(x**(1/2)+1)):
        if x % i == 0:
            return False
        
    return True

def solution(n, k):
    # 1. k진수로 변환
    result_mod = ''

    while n > 0:
        division, mod = divmod(n, k)  # 몫과 나머지
        result_mod += str(mod)  # 나머지는 계속해서 append

        n = division  # 다음 나눗셈을 위해 업데이트


    k_number = result_mod[::-1]  # k진수 구하기

    # 2. 소수 개수 구하기
    # 소수: 1보다 큰 수 중 약수가 자기 자신과 1만 있는 수
    number_list = k_number.split('0')

    answer = 0
    for n in number_list:
        if n and is_prime_number(int(n)):
            answer+=1

    return answer


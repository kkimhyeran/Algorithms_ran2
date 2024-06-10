# 1. 입력값 받기
n = int(input())

char_list = []
for _ in range(n):
    char_list.append(input())
# char_list = ['ACDEB', 'GCF']

# 2. 각 알파벳별 자릿수 확인 
# 우선 순위를 부여하기 위해 (예: A가 다섯자리 문자에서 첫번째 등장 > 10000
# C가 첫번째 문자에서는 두번째 등장, 두번쨰 문자에서는  두번째 등장 > 1010)

digit_dict = {}

for char in char_list:
    for i in range(len(char)):
        # 해당 문자의 자릿수가 있다면
        if char[i] in digit_dict.keys():
            digit_dict[char[i]] = digit_dict[char[i]] + (10 ** (len(char) - 1 - i))
        else:
            digit_dict[char[i]] = 10 ** (len(char) - 1 -i)

# 3. 알파벳 자릿수에 따라서 우선순위 부여
# 가장 큰 자릿수 숫자 > 9 부여
char_orders_dict = {}
digit_order_dict = sorted(digit_dict.items(), key=lambda x: x[1], reverse=True)

start_number = 9
for digit in digit_order_dict:
    char_orders_dict[digit[0]] = start_number
    start_number -= 1

# 4. 단어 > 숫자로 변환
# 우선순위를 기준으로 단어 - 숫자에 선택된거 기준으로 바꾸기
char_to_num_list = []
for char in char_list:
    char_to_num = ''

    for s in char:
        char_to_num += str(char_orders_dict[s])

    char_to_num_list.append(int(char_to_num))

# 5. 최대 합 구하기
# 숫자로 변환된 값들의 합을 출력
print(sum(char_to_num_list))
import sys
input = sys.stdin.readline

t = int(input())

result = []
for _ in range(t):
    n = int(input())
    number_list = [input().strip() for _ in range(n)]

    # 문자열 그대로 정렬
    number_list.sort()

    is_valid = True
    for i in range(n - 1):
        if number_list[i + 1].startswith(number_list[i]):
            is_valid = False
            break

    result.append(is_valid)

for rst in result:
    print('YES' if rst else 'NO')

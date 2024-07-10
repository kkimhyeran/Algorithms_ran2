'''
@ No        : 18310
@ Title     : 안테나
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 집의 수
    - addr_list : n개 집 위치
@ 출력값
    - 안테나가 설치될 위치 (단, 여러개 일 경우 작은 위치 값을 출력)
'''



n = int(input())
addr_list = list(map(int, input().split()))
addr_list.sort()

if len(addr_list) % 2 == 0:
    idx = len(addr_list) //2
    result = addr_list[idx-1]
else:

    idx = len(addr_list) // 2
    result = addr_list[idx]
    
    
print(result)

# 0. 필요한 라이브러리 import
import sys
import heapq

# 1. 강의 시간표 개수와 정보 입력받기
n = int(sys.stdin.readline())
time_tables = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])


# 2. 강의 시간표에 따라서 강의실 배분하기
room = []
heapq.heappush(room, time_tables[0][1])


for i in range(1, n):
    if time_tables[i][0] < room[0]: 
        heapq.heappush(room, time_tables[i][1])  
    else:  
        heapq.heappop(room)  
        heapq.heappush(room, time_tables[i][1])  
        
        
# 3. 강의실 개수 출력
# 현재 deque에 남아있는 값의 개수 = 강의실 개수
print(len(room))
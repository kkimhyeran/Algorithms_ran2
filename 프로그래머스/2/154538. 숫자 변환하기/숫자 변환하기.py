from collections import deque
def solution(x, y, n):
    
    if x == y:
        return 0
    # y -> x 로 가는 방법으로 해서 구하기
    cnt = 0
    q = deque()
    q.append([y, cnt])
    answer = -1
    
    while q:
        # print(q)
        now = q.popleft()
        cnt = now[1] + 1
        
        if now[0] == x:
            answer = now[1]
            break
        
        else:
            if now[0] > x:
                
                if now[0] % 3 == 0:
                    q.append([now[0]//3, cnt])
                    
                if now[0] % 2 == 0:
                    q.append([now[0]//2, cnt])
                
                q.append([now[0]-n, cnt])
                
    if answer:
        return answer
    else:
        return -1
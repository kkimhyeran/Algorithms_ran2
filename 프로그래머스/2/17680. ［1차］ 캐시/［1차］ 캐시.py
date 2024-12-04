from collections import deque

def solution(cacheSize, cities):
    
    q = deque([])
    cities = [city.lower() for city in cities]
    
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    else:
        for city in cities:

            # 캐시되지 않으면
            if city not in q:
                answer += 5

                if len(q) >= cacheSize:
                    q.popleft()

                q.append(city)

            # 캐시되어 있으면
            else:
                # 캐시 갱신
                q.remove(city)
                q.append(city)
                answer += 1
                
                # if len(q) >= cacheSize:
                #     q.popleft()
                
    return answer
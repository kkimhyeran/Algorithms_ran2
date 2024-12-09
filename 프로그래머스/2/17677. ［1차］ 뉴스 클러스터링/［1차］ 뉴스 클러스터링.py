from collections import Counter

def split_words(s):
    a = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            a.append(s[i]+ s[i + 1])
    return a


def solution(str1, str2):
    
    # 1. str1, str2 두 글자씩 끊기
    str1_splits = split_words(str1.lower())
    str2_splits = split_words(str2.lower())
    
    
    # 2. 합집합 구하기
    counter1 = Counter(str1_splits)
    counter2 = Counter(str2_splits)
    
    intersection = counter1 & counter2  # 교집합 (각 원소의 최소 개수)
    union = counter1 | counter2        # 합집합 (각 원소의 최대 개수)
    
    intersection_size = sum(intersection.values())
    union_size = sum(union.values())
    
    # 4. 자카드 유사도 구하기
    if union_size == 0:  # 공집합 처리
        jaccard_similarity = 1
    else:
        jaccard_similarity = intersection_size / union_size
    
    # 6. 결과값 반환 (65536을 곱한 후 정수로 변환)
    return int(jaccard_similarity * 65536)
    
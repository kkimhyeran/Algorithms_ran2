from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for size in course:
        
        order_combinations = []
        
        for order in orders:
            order_combinations += combinations(sorted(order), size)
        # print(order_combinations)
        
        most_ordered = Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
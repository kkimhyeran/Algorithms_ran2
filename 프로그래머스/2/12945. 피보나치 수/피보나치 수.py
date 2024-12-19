import sys
sys.setrecursionlimit(10*7)

def solution(n):
    if n < 2:
        return n
    else:
        num1 = 0
        num2 = 1
        
        for _ in range(2, n + 1):
            num1, num2 = num2, num1 + num2
        return num2 % 1234567
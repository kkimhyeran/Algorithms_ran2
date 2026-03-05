import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

print(1 if T == S else 0)
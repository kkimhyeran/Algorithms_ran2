def count_paper(x, y, n):
    first_clr = matrix[x][y]

    global white
    global blue

    for i in range(x, x + n):
        for j in range(y, y + n):

            if first_clr != matrix[i][j]:
                count_paper(x, y, n//2) # 1사분면
                count_paper(x + n//2, y, n//2) # 2사분면
                count_paper(x, y + n//2, n//2) # 3사분면
                count_paper(x + n//2, y + n//2, n//2) # 4사분면
                return

    if first_clr == 0:
        white += 1
    else:
        blue += 1


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
white = 0
blue = 0

count_paper(0, 0, n)
print(white)
print(blue)
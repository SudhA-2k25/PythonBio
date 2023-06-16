# DYNAMIC TIME WRAPPING
import math

t = [1, 1, 2, 2, 3, 5]
s = [1, 2, 3, 5, 5, 6]

col = len(t)
row = len(s)
tw = [[0] * (col + 1) for i in range(row + 1)]

for i in range(1, row + 1):
    tw[i][0] = math.inf

for i in range(1, col + 1):
    tw[0][i] = math.inf

for i in range(1, row + 1):
    for j in range(1, col + 1):
        diag = tw[i - 1][j - 1]
        left = tw[i - 1][j]
        up = tw[i][j - 1]

        tw[i][j] = abs(s[i - 1] - t[j - 1]) + min(diag, left, up)

for i in range(1, row + 1):
    for j in range(1, col + 1):
        print(tw[i][j], end="\t")
    print()

sum_val = tw[row][col]
print(f"The optimal edge is {sum_val}")



i = row
j = col
count = 0

while i > 0 and j > 0:
    diag = tw[i - 1][j - 1]
    left = tw[i - 1][j]
    up = tw[i][j - 1]

    if min(diag, left, up) == diag:
        i -= 1
        j -= 1
        sum_val += diag
        count += 1

    elif min(diag, left, up) == left:
        i -= 1
        sum_val += left
        count += 1

    elif min(diag, left, up) == up:
        j -= 1
        sum_val += up
        count += 1

optimal_path = sum_val / count
print(f"The optimal alignment path value is {optimal_path}")

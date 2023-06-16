#LCS (substring)
s = "MALAYALAM"
t = "LAYA"

ls = len(s) + 1
lt = len(t) + 1

lcs = [ [0] * lt for i in range(ls) ]

for i in range(1, ls):
    for j in range(1, lt):
        if s[i - 1] == t[j - 1]:
            lcs[-i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

for i in range(ls):
    for j in range(lt):
        print(lcs[i][j], end="\t")
    print()

# Backtrace
start = lcs[ls - 1][lt - 1]
i = ls - 1
j = lt - 1

while i >= 0 and j >= 0 and start > 0:
    print(start, end="\t")
    if s[i - 1] == t[j - 1]:
        start = lcs[i - 1][j - 1]
        i -= 1
        j -= 1
    else:
        if lcs[i - 1][j] >= lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1
        start = lcs[i][j]

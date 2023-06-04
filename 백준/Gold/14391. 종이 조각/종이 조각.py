from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
paper, ans = [], []
for _ in range(n):
    paper.append(list(map(int, input().strip())))

for i in range(1 << n*m):
    total = 0
    for row in range(n):
        rowsum = 0
        for col in range(m):
            idx = row * m + col
            # print(idx, row, col, i, i &(1 << idx), (1 << idx))
            if i & (1 << idx) != 0:
                rowsum = rowsum * 10 + paper[row][col]
                # print(rowsum, paper[row][col], total)
            else:
                total += rowsum
                rowsum = 0
        total += rowsum
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row * m + col
            if i & (1 << idx) == 0:
                colsum = colsum * 10 + paper[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)
print(max(ans))
# print(8 & (1<<1))
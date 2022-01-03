import sys
N = int(sys.stdin.readline())
bomboni = []
for _ in range(3):
    candies = list(sys.stdin.readline().strip())
    bomboni.append(candies)
print(bomboni)
for i in range(len(bomboni)):
    # print(bomboni[i].count("C"))
    print(max(bomboni[i]))
# 가장 긴 행 찾기
# for i in range(1,len(bomboni)):
#     if bomboni[i-1]!= bomboni[i]:
#         temp = bomboni[i-1]
#         bomboni[i-1] = bomboni[i]
#         bomboni[i] = temp
# for i in range(len(bomboni)):
#     for j in range(1,len(bomboni[i])):
#         if bomboni[j-1]!= bomboni[j]:
#             temp = bomboni[j-1]
#             bomboni[j-1] = bomboni[j]
#             bomboni[j] = temp
#     print(bomboni[i])
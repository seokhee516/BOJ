# import sys
# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split(' ')))
# P = list(map(int, sys.stdin.readline().split(' ')))

N = 4
L = [2,3,1]
P = [5,2,4,1]

result = 100000000
for i in range(len(L)):
    print(i)
    print(P[i:])






# result = 100000000
# temp = 0
# temp2 = 0
# for i in range(len(L)):
#     temp += P[i] * sum(L[i:])
#     if temp < result:
#         result = temp
#     temp = 0
#     temp += P[i] * L[i] +temp2
#     temp2 += P[i] * L[i]
# print(result)
# print(sum(L[0:]))

# m += L[0] * P [0]
# for i in range(1, len(L)):
#     L[i]
# from itertools import combinations
# result=[]

# for i in range(1, len(L[1:])+1):
#     c=combinations(L[1:],i)
#     result.extend(c)

# print(result)
# for r in result:
#     # print(sum(r))
#     for j in range(1, len(P)-1):
#         print(sum(r)*P[j])
#     print("-")
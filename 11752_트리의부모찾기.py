import sys
# sys.setrecursionlimit(100000) #런타임 에러 방지
# N = int(input())
# N = int(sys.stdin.readline().strip())
# tree = {1:0}
# for _ in range(N-1):
#     x, y = map(int, sys.stdin.readline().strip().split())
#     if x not in tree.keys():
#         tree[x] = y
#     else:
#         tree[y] = x

# for i in range(2, N+1):
#     print(tree[i])
N = int(sys.stdin.readline().strip())
tree = [0] * (N + 1)
tree[1] = -1
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().strip().split())
    if tree[x] != 0:
        tree[y] = x
    else:
        tree[x] = y
for i in range(2, N+1):
    print(tree[i])

print(tree)
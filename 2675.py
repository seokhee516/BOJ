import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(str, sys.stdin.readline().strip().split(' '))
    K = list(K)
    for i in range(len(K)):
        print(K[i]*int(N), end='')
    print()

# print(list('ABC'))
import sys
input = sys.stdin.readline

S = set()
M = int(input())
for i in range(M):
    X = input().strip().split()
    if X[0] == 'add':
        S.add(int(X[1]))
    elif X[0] == 'remove':
        try:
            S.remove(int(X[1]))
        except:
            pass
    elif X[0] == 'check':
        if int(X[1]) in S:
            print(1)
        else:
            print(0)
    elif X[0] == 'toggle':
        if int(X[1]) in S:
            S.remove(int(X[1]))
        else:
            S.add(int(X[1]))
    elif X[0] == 'all':
        S.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif X[0] == 'empty':
        S = set()
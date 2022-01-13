import sys

A, B = map(int, sys.stdin.readline().split(' '))
C, D = map(int, sys.stdin.readline().split(' '))
E, F = map(int, sys.stdin.readline().split(' '))
X=Y=0
if A==C and A!=E:
    X = E
elif C==E and A!=E:
    X = A
elif A==E and C !=E:
    X = C
    
if B==D and B!=F:
    Y = F
elif D==F and B!=F:
    Y = B
elif B==F and D!=F:
    Y = D
print(X, Y)
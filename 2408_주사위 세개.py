import sys 

input = sys.stdin.readline
A, B, C = map(int, input().split())
answer = 0
if A == B and B == C:
    answer = 10000+A*1000
elif A == B and B != C:
    answer = 1000+A*100
elif A == C and B != C:
    answer = 1000+A*100
elif B == C and A != C:
    answer = 1000+B*100
elif A != B and B != C:
    answer = max(A, B, C)*100
print(answer)
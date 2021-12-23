import sys
import statistics
N = int(sys.stdin.readline())
X = list(int(sys.stdin.readline()) for _ in range(N))
print(round(statistics.mean(X)))
print(statistics.median(X))
if N ==1:
    print(X[0])
else:
    if len(statistics.multimode(X)) > 1:
        print(sorted(statistics.multimode(X))[1])
    else:
        print(statistics.multimode(X)[0])
print(max(X)-min(X))

import sys
T = int(sys.stdin.readline().strip())
def apt(n, k):
    if n == 1:
        return int(k*(k+1)/2)
    answer = 0
    for i in range(1, k+1):
        answer += apt(n-1, i)

    return int(answer)

for _ in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip()) 
    print(apt(k, n))
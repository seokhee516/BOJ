import sys
T = int(sys.stdin.readline().strip())

def fibo(n):
    previous = [1, 0]
    current = [0, 1]
    if n == 0:
        return previous
    elif n == 1:
        return current
    else:
        for i in range(1,n):
            temp = current.copy()
            current[0] += previous[0]
            current[1] += previous[1]
            previous = temp
        return current

for _ in range(T):
    result = fibo(int(sys.stdin.readline().strip()))
    print(result[0], result[1])
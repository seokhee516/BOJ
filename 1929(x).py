import time
start = time.time()
import sys
# M, N = map(int, sys.stdin.readline().split(' '))
M, N = map(int, '3 16'.split(' '))
for number in range(M, N+1):
    factor = 0
    for n in range(2, number):
        if number % n ==0:
            factor+=1
            break
    if factor == 0:
        print(number)

end = time.time()
print(end)

# 시간초과

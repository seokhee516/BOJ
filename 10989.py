'''
메모리 고려한 정렬
'''
import sys
N = int(sys.stdin.readline())
num = [0] * 10001
for _ in range(N):
    num[int(sys.stdin.readline())] += 1
for i in range(10001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)
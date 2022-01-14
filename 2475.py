import sys
num = [i**2 for i in map(int, sys.stdin.readline().strip().split(' '))]
print(sum(num)%10)
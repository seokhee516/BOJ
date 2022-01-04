import sys
S = int(sys.stdin.readline())
num = 1
while num*(num+1)//2 <= S:
    num += 1
print(num-1)
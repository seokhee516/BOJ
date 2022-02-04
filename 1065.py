def check_han(num):
    num = list(str(num))
    d = int(num[1])- int(num[0])
    for i in range(1, len(num)-1):
        tmp = int(num[i+1])- int(num[i])
        if d != tmp:
            return False
        return True

import sys
N = int(sys.stdin.readline().strip())
han = 0
if N < 100:
    han += N
else:
    han += 99
    for num in range(100, N+1):
        if check_han(num):
            han +=1
print(han)
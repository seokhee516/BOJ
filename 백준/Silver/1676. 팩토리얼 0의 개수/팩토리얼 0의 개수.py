import math
n = str(math.factorial(int(input())))
ans = 0
for i in range(len(n)-1,-1,-1):
    if n[i] != '0':
        break
    else:
        ans += 1
print(ans)
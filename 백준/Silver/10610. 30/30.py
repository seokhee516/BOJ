import sys
input = sys.stdin.readline

n = list(input().strip())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n: # 각 자릿수의 합이 3으로 나누어 떨어지지 않거나 일의 자릿수가 0이 아니라면 30의 배구가 아님
    print(-1)
else:
    print(''.join(n))

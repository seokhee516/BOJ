import sys
ans = int(sys.stdin.readline())
num = ans // 2
# ans = 20
# num = 18
# try:
num_sum = 0
while num <= ans:
    num_sum = 0
    num = str(num)
    for i in range(len(list(num))):
        num_sum += int(list(num)[i])
    num_sum += int(num)
    if num_sum != ans:
        num = int(num)
        num += 1
    elif num_sum == ans:
        print(num)
        break
    if int(num) > ans:
        print(0)
        break
# except:
#     print(0)
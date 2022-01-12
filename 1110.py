import sys
N = sys.stdin.readline().strip()
num_list = list(N)
new_num = 0
temp = 0
cnt = 0
while True:
    if int(N) < 0:
        N = '0' + N
    
    for num in num_list:
        temp += int(num)
    temp = temp % 10
    new_num = int(num_list[-1] + str(temp))
    cnt += 1
    if new_num == int(N):
        break
    num_list = list(num_list[-1] + str(temp))
print(cnt)
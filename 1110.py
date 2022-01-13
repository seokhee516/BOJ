import sys
N = sys.stdin.readline().strip()
original_N = N
cnt = 0
while True:
    if int(N) < 10:
        N = '0' + str(int(N))
    N_list = list(N)
    sum_number = int(N_list[0]) + int(N_list[1])
    sum_number_list = list(str(sum_number))
    new_N = N_list[-1] + sum_number_list[-1]
    cnt += 1
    if int(original_N) == int(new_N):
        break
    else:
        N = new_N
print(cnt)
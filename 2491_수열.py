N = 9
# lst = [1,2,2,7,9,5,6,7,8]
lst = [4, 1, 3, 3, 2, 2, 9, 2, 3]
cnt_asc = [1]
for i in range(1, N):
    if lst[i-1] == lst[i] or lst[i-1]+1 == lst[i]:
        cnt_asc[-1] += 1
    else:
        cnt_asc.append(1)
# print(max(cnt_asc))

cnt_desc = [1]
for i in range(N-1, -1, -1):
    print(lst[i])

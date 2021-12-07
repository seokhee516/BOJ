'''
idx :  1 2 3 4 5 6 7 8 9

num:   1 2 2 3 3 3 4 4 4 4

이니깐 2 + 3 + 3 + 3 + 4 = 15 죠
'''

A, B = map(int, input().split(' '))
num = []
ans = 0
for i in range(1, 1000+1):
    for j in range(1, i+1):
        num.append(i)
    if len(num) >= B:
        break
for n in range(A-1, B):
    ans += num[n]
print(ans)


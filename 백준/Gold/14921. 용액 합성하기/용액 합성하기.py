import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

# 시간초과
# answer = 1e9
# for i in range(n-1):
#     for j in range(i+1, n):
#         if abs(answer) > abs(lst[i]+lst[j]):
#             answer = lst[i]+lst[j]
# print(answer)

i = 0 
j = n-1
answer = lst[i] + lst[j]
while i < j:
    now = lst[i] + lst[j]
    if abs(answer) > abs(now):
        answer = now
    if now < 0: # 음수 값일 경우 키워줌
        i += 1
    else: # 양수 값일 경우 줄여줌
        j -= 1
        
print(answer)
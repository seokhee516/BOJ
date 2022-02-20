import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

# 오름차순 
cnt_asc = [1] # 수열 길이 리스트 1이 기본
for i in range(1, N): # 맨 앞에서 하나 뒤부터 시작
    if lst[i-1] <= lst[i]: # 앞에거보다 뒤에거가 크면
        cnt_asc[-1] += 1 # 수열 길이 리스트에 1 더하기
    else:
        cnt_asc.append(1) # 아닐경우 수열 길이 리스트 1로 초기화

# 내립차순
cnt_desc = [1] # 수열 길이 리스트 1이 기본
for i in range(N-2, -1, -1): # 맨 뒤에서 하나 앞 부터 시작
    if lst[i] >= lst[i+1]: # 앞에거보다 뒤에거가 작으면
        cnt_desc[-1] += 1 # 수열 길이 리스트에 1 더하기
    else:
        cnt_desc.append(1) # 아닐경우 수열 길이 리스트 1로 초기화


print(max(max(cnt_asc),max(cnt_desc))) # 오름차순 내림차순 수열 길이 중 가장 큰 값

import sys
input = sys.stdin.readline
# 나무의 개수(N)와 집으로 가져가려고 하는 나무의 길이(M)을 입력받기
n, m = map(int, input().split())
# 각 나무의 개별 높이 정보 입력 받기
array = list(map(int, input().split()))
# 오름 차순 정렬
array.sort()
# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(array) # 가장 큰 나무의 길이가 end 

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0 # 잘린 나무의 길이 합
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 나무의 길이 계산
        if x > mid:
            total += x - mid
    # 나무의 길이가 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    # 나무의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else: # 크거나 같을 때 처리
        result = mid # 최대한 덜 잘렸을 때가 정답이므로, 여기에서 result기록 
        start = mid + 1
print(result)

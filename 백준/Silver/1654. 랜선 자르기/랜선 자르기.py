'''
4 11
802
743
457
539
'''
import sys
input = sys.stdin.readline

# 랜선의 개수 K, 필요한 랜선의 개수 N
k, n = map(int, input().split())
# 랜선의 길이
array = [int(input()) for _ in range(k)]

# 이진 탐색을 위한 시작 점과 끝점 설정
start = 1 # 랜선의 길이가 0이 되면 안되므로 시작 점 1로 설정
end = max(array)

# 이진 탐색 수행
result = 0 # 핸선의 최대 길이
while start <=end:
    total = 0 # 잘린 랜선으로 만들 수 있는 개수
    mid = (start + end) // 2
    for x in array:
        total += (x // mid)
    # 랜선의 개수가 부족한 경우
    if total < n:
        end = mid -1 
    # 랜선의 개수가 많거나 같은 경우
    else:
        result = mid
        start = mid + 1
print(result)
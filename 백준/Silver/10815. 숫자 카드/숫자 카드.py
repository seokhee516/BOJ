import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return 1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 end <- mid-1
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    # 중간 점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 start <- mid+1
    else:
        return binary_search(array, target, mid + 1, end)

# 숫자 카드
n = int(input())
card = list(map(int, input().split()))
# 확인해야 할 숫자
m = int(input())
data = list(map(int, input().split()))
# 오름 차순 정렬
card.sort()

for i in range(m):
    print(binary_search(card, data[i], 0, n-1), end =' ') 
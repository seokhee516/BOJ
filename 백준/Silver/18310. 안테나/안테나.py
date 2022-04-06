n = int(input())
array = list(map(int, input().split()))
array.sort()
mid = (0 + n-1) // 2
print(array[mid])
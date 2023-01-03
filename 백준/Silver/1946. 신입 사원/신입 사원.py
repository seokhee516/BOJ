t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a,b))
    arr.sort(key=lambda x:x[0])
    ans = 1
    tmp = arr[0][1]
    for i in range(1,n):
        if tmp > arr[i][1]:
            ans += 1
            tmp = arr[i][1]
    print(ans)
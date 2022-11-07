def bin_s(n, target):
    s = 0
    e = n - 1
    while s<=e:
        m = (s+e) // 2
        if num1[m] == target:
            return 1
        elif num1[m] < target:
            s = m + 1
        else:
            e = m - 1
    return 0
            
t = int(input())
for _ in range(t):
    n = int(input())
    num1 = list(map(int, input().split()))
    num1.sort()
    m = int(input())
    num2 = list(map(int, input().split()))
    for i in num2:
        print(bin_s(n, i))
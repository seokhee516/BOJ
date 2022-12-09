h, w = map(int, input().split())
block = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(block[:i])
    right_max = max(block[i:])

    cur = min(left_max, right_max)
    ans += max(0,cur - block[i])

print(ans)
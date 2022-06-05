import sys
import math
input = sys.stdin.readline
D, H, W = map(int, input().split())
x = D*H / (H**2 + W**2)**0.5
y = D*W / (H**2 + W**2)**0.5
print(math.floor(x), math.floor(y))

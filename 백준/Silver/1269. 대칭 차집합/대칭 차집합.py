import sys
input = sys.stdin.readline
a, b = map(int, input().split())
s_a = set(map(int, input().split()))
s_b = set(map(int, input().split()))
print(len(s_a-s_b) + len(s_b-s_a))
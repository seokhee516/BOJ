import sys
from itertools import product
from itertools import combinations_with_replacement
input = sys.stdin.readline
n = int(input())
rome = [1,5,10,50]
# print(len(set(map(lambda x : sum(x), product(rome, repeat=n))))) # 시간초과
# print(list(product(rome, repeat=n)))
# print(len(set(combinations_with_replacement(rome, n))))
print(len(set(map(lambda x : sum(x), combinations_with_replacement(rome, n)))))
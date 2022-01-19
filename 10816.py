import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
card = Counter(list(map(int, sys.stdin.readline().strip().split(' '))))
M = int(sys.stdin.readline().strip())
card_num = list(map(int, sys.stdin.readline().strip().split(' ')))
for i in card_num:
    print(card[i], end = ' ')
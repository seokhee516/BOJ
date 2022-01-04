import sys
N = int(sys.stdin.readline())
word = []
for i in range(N):
    word.append(sys.stdin.readline().strip())
word = sorted(list(set(word)))
word = sorted(word, key=len)
for x in word:
    print(x)
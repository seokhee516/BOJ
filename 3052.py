
import sys
a=[]
for _ in range(10):
    a.append(int(sys.stdin.readline())%42)
a=set(a)
a=list(a)
print(len(a))
# print(84 % 42)
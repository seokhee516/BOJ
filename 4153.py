import sys
while True:
    a, b, c = sorted(map(int, sys.stdin.readline().split(' ')))
    
    print(a, b, c)
    if (a==0) or (b==0) or (c==0):
        break
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")

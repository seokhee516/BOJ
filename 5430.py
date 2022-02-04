import sys
# from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    p = list(sys.stdin.readline().strip().replace('RR',''))
    n = int(sys.stdin.readline().strip())
    rev = 0
    try:
        arr = sys.stdin.readline().strip()
        
        arr = arr[1:-1].split(",")
        
        for func in p:
            if func == 'R':
                rev += 1
            elif func == 'D':
                if rev % 2 != 0:
                    arr = arr[:-1]
                else:
                    arr = arr[1:]
                if arr == '[]':
                    raise
        if rev % 2 != 0:
            print('['+','.join(reversed(arr))+']')
        else:
            print('['+','.join(arr)+']')
    except:
        print("error")


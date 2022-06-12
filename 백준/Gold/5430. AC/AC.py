import sys
input = sys.stdin.readline

head, size, dir = None, None, None

def init():
    global head, size, dir
    head, size, dir = 0, 0, 0

def reverse():
    global head, size, dir

    if dir == 0:
        head = head + size - 1
        dir = 1
    else:
        head = head - size + 1
        dir = 0
def delete():
    global head, size, dir

    if size == 0:
        return False
    elif dir == 0:
        head = head + 1
        size = size - 1
    else:
        head = head - 1
        size = size - 1
    return True

def printarr(arr):
    if dir == 0:
        tmp = arr[head:head + size]
    else:
        tmp = arr[head - size + 1:head + 1]
        tmp.reverse()
    print('[%s]'%','.join(tmp))

def run(cmd, arr):
    global head, size, dir

    for ch in cmd:
        if ch == 'R':
            reverse()
        elif ch == 'D':
            if delete() == False:
                print('error')
                return
    printarr(arr)

T = int(input())
    
for tc in range(T):
    init()
    cmd = input().strip()
    size = int(input())
    arr = input().strip()[1:-1].split(',')
    run(cmd, arr)
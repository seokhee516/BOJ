import sys
T = int(sys.stdin.readline())

for _ in range(T):
    VPS = list(sys.stdin.readline().strip())
    check = 0
    for i in range(len(VPS)):
        if VPS.pop() == ')':
            check += 1
        else:
            check -= 1
            if check < 0:
                break
        
    if (len(VPS) == 0) & (check==0):
        print('YES')
    else:
        print('NO')
    


# VPS = list('(()())((()))')

# check = 0

# for i in range(len(VPS)):
#     if VPS.pop() == ')':
#         check += 1
#     else:
#         check -= 1
#         if check < 0:
#             break
    
# if (len(VPS) == 0) & (check==0):
#     print('YES')
# else:
#     print('NO')
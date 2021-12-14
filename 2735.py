import sys
T = int(sys.stdin.readline())
if (T % 100 == 0) & (T % 400 != 0):
    print(0)
elif ((T % 4 == 0) & (T % 100 != 0)) | ((T % 100 == 0) & (T % 400 == 0)):
    print(1)
else:
    print(0)
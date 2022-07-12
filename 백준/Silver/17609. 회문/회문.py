import sys
input = sys.stdin.readline
def palindrome(string):
    for i in range(len(string)//2):
        j = len(string) -1 -i
        if string[i] != string[j]:
            return (i, j)
    return 1

t = int(input())
for _ in range(t):
    s = input().strip()
    ret = palindrome(s)
    if ret == 1:
        print(0)
    else:
        i, j = ret[0], ret[1]
        if palindrome(s[:i]+s[i+1:]) == 1 or palindrome(s[:j]+s[j+1:]) == 1:
            print(1)
        else:
            print(2)

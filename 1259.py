import sys
palindrome = list(sys.stdin.readline().strip())
while int(palindrome[0]) != 0:
    # if len(palindrome) % 2 ==0:
    #     print("no")
    # else:
    for i in range(0, len(palindrome)//2+1):
        if palindrome[i] != palindrome[-i-1]:
            print("no")
            break
        elif i == len(palindrome)//2:
            print("yes")
    palindrome = list(sys.stdin.readline().strip())
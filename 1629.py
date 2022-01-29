import sys
A, B, C = map(int, sys.stdin.readline().strip().split())
def multiply(A, B):
    if B==0:
        return A
    A *= A
    B -= 1
    return multiply(A, B)

print(multiply(A, B)% C)
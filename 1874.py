
import sys
stack = []
sequence = [0]
answer = []

stack = list(range(int(sys.stdin.readline().strip()), 0, -1))

def getItem(sequence, stack, answer, num):
    while sequence[-1] < num:
        sequence.append(stack.pop())
        answer.append('+')
    sequence.pop()
    answer.append('-')
    
    return sequence, stack, answer
try:
    for _ in range(len(stack)):
        num = int(sys.stdin.readline().strip())
        sequence, stack, answer = getItem(sequence, stack, answer, num)

    for a in answer:
        print(a)
except:
    print("NO")



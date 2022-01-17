import sys
stack = []
sequence = []

for i in range(8,0,-1):
    stack.append(i)
print(stack)

# sequence.append(stack.pop()) # push
# sequence.append(stack.pop()) 
# sequence.append(stack.pop())
# sequence.append(stack.pop())
# print(sequence.pop()) # pop
# print(sequence.pop())
# sequence.append(stack.pop())
# sequence.append(stack.pop())
# print(sequence.pop())
# sequence.append(stack.pop())
# sequence.append(stack.pop())
# print(sequence.pop())
# print(sequence.pop())
# print(sequence.pop())
# print(sequence.pop())
# print(sequence.pop())

n = int(sys.stdin.readline())
old_k = 0
for _ in range(n):
    new_k = int(sys.stdin.readline())
    if new_k < old_k:
        while sequence[-1] != new_k-1:
            print(sequence.pop())
    else:
        if stack[-1] < new_k:
            while stack[-1] != new_k+1:
                sequence.append(stack.pop())
    old_k = new_k






# stack = []
# sequence = []

# for i in range(5,0,-1):
#     stack.append(i)
# print(stack)

# sequence.append(stack.pop()) # push
# print(sequence.pop()) # pop

# sequence.append(stack.pop()) 
# print(sequence.pop())

# sequence.append(stack.pop())
# sequence.append(stack.pop())
# sequence.append(stack.pop())
# print(sequence.pop())

# print(sequence.pop())
# print(sequence.pop())

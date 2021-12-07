n = int(input())

for _ in range(n):
    input_list = [int(x) for x in input().split(' ')]
    print(sorted(input_list)[-3])


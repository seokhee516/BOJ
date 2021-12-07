# list_1 = [[1]]
# list_2 = []

# list_2.append(list_1[0])
# list_1 = list_2

# print(list_1)

# for i in list_1:
#     # print(list_1)
#     list_2.append(i)

# print(list_1)

# 1978
number = int(input())
input_data = list(map(int, input().split(' ')))

cnt = 0
cd = 0
for n in range(number):
    if input_data[n] > 1:
        for i in range(1, input_data[n]+1):
            if input_data[n] % i ==0:
                cd += 1
    if cd == 2:
        cnt+=1
    cd=0

print(cnt)
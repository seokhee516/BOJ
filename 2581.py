input_data = []
for _ in range(2):
    input_data.append(int(input()))
cd = 0
decimal_list =[]
for number in range(input_data[0],input_data[1]+1):
    for n in range(1,number+1):
        if number  % n == 0:
            cd += 1
            if cd > 2:
                break
    if cd == 2:
        decimal_list.append(n)
    cd =0
if decimal_list == []:
    print(-1)
else:
    print(sum(decimal_list))
    print(decimal_list[0])
num = '0001100'
# num = "00"
ans = 0
if '0' in num and '1' in num:
    print("no")
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            ans += 1
        print(num[i])
    
else:
    print(0)
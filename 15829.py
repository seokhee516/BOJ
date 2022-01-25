N = int(input())
input_data = input()
ans = 0
for i in range(N):
    ans += (ord(input_data[i])-96)*(31**i)
print(ans % 1234567891)
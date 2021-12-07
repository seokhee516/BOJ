A, B = map(int, input().split())
gcd = 0
gcm = 0
for i in range(1, A+1):
    if A % i ==0:
        if B % i == 0:
            gcd = i
print(gcd)
gcm =(A // gcd) * (B // gcd) * gcd
print(gcm)

import sys
sugar = int(sys.stdin.readline())
temp = sugar
bongi = -1
for i in range(sugar // 5 + 1):
    if (temp-(i*5)) % 3 == 0:
        sugar = temp
        sugar = sugar-(i*5)
        bongi = i + (sugar//3)
print(bongi)
import sys
input_data = list(sys.stdin.readline().strip())
num = 0
for dial in input_data:
    # if (ord(dial)) <= 65:
    #     num += 2
    if (ord(dial)) <= 67:
        num += 3
    elif (ord(dial)) <= 70:
        num += 4
    elif (ord(dial)) <= 73:
        num += 5
    elif (ord(dial)) <= 76:
        num += 6
    elif (ord(dial)) <= 79:
        num += 7
    elif (ord(dial)) <= 83:
        num += 8
    elif (ord(dial)) <= 86:
        num += 9
    elif (ord(dial)) <= 90:
        num += 10
print(num)
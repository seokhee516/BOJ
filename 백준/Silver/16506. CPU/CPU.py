import sys
input = sys.stdin.readline

op = {"ADD": 0, "ADDC": 1, "SUB": 2, "SUBC": 3, "MOV": 4, "MOVC": 5,
      "AND": 6, "ANDC": 7, "OR": 8, "ORC": 9, "NOT": 10, "MULT": 12,
      "MULTC": 13, "LSFTL": 14, "LSFTLC": 15, "LSFTR": 16, "LSFTRC": 17,
      "ASFTR": 18, "ASFTRC": 19, "RL": 20, "RLC": 21, "RR": 22, "RRC": 23}
t = int(input())
for _ in range(t):
    data = input().strip().split()
    output = ''
    output += bin(op[data[0]])[2:].zfill(5) + '0'
    output += bin(int(data[1]))[2:].zfill(3)
    output += bin(int(data[2]))[2:].zfill(3)
    if data[0][-1] =='C':
        output += bin(int(data[3]))[2:].zfill(4)
    else:
        output += bin(int(data[3]))[2:].zfill(3) + '0'
    print(output)
d = {}
for i in range(97,123):
    d[chr(i)] = 0

string = input().strip()
for s in string:
    d[s] += 1
for v in d.values():
    print(v, end = " ")
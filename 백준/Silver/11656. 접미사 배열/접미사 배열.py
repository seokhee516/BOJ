s = input().strip()
lst = [s[i:] for i in range(len(s))]
lst.sort()
for l in lst:
    print(l)
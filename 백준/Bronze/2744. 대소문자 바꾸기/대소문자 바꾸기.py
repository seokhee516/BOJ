st = input().strip()
ans = []
for s in st:
    if s.isupper():
        ans.append(s.lower())
    else:
        ans.append(s.upper())
print("".join(ans))
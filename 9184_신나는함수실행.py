a = 10
b = 4
c = 6
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        # print("리턴 1")
        return 1

    if a < b and b < c:
        # print(f"a가 가장 작으면: w({a}, {b}, {c-1}) + w({a}, {b-1}, {c-1}) - w({a}, {b-1}, {c})")
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        # print(f"그렇지 않으면: w({a-1}, {b}, {c}) + w({a-1}, {b-1}, {c}) + w({a-1}, {b}, {c-1}) - w({a-1}, {b-1}, {c-1})")
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

print(w(a,b,c))
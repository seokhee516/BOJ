def solution(s):
    sp = list(map(int, s.split(' ')))
    mi, ma = min(sp), max(sp)
    return f"{mi} {ma}"
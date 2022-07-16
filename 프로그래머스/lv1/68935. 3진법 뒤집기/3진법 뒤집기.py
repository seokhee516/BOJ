def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return int(rev_base, 3)
def solution(n):
    answer = change(n, 3)
    return answer
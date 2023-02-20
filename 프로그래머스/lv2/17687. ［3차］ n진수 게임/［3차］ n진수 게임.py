def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]

def solution(n, t, m, p):
    ans = ''
    tot = ''
    for i in range(m*t+1):
        tot += convert(i,n)
    for k in range(p-1,m*(t-1)+p,m):
        ans += tot[k]
    # print(tot)
    # print(ans)
    return ans
a, b = map(int, input().split())
# 유클리드 호제법
def gcd(x,y):
    mod = x%y # 나머지
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y
print('1'*gcd(a,b))
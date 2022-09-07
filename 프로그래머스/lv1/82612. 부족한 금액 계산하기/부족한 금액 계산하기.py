def solution(price, money, count):
    s = (count*(price+price*count)) / 2
    ans = s - money
    if ans < 0: ans = 0
    return ans
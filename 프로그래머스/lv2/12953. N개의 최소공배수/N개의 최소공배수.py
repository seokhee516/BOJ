def solution(arr):
    def gcd(a,b):
        while b >0:
            a,b = b, a%b
        return a
    def lcm(a,b):
        return a*b / gcd(a,b)
    answer = 1
    for item in arr:
        answer = lcm(answer, item)
    return answer
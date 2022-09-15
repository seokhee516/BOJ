def fun(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt % 2 == 0:
        return num
    else:
        return -num
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += fun(i)
    return answer
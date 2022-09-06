def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b
    for i in range(a-1):
        day += month[i]
    d = day % 7
    if d == 1:
        answer = 'FRI'
    elif d == 2:
        answer = 'SAT'
    elif d == 3:
        answer = 'SUN'
    elif d == 4:
        answer = 'MON'
    elif d == 5:
        answer = 'TUE'
    elif d == 6:
        answer = 'WED'
    elif d == 0:
        answer = 'THU'
    return answer
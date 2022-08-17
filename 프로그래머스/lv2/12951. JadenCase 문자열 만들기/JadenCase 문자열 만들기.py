def solution(s):
    answer = ''
    lst = list(s)
    start = 0
    for i in range(len(lst)):
        if start == 0:
            lst[i] = lst[i].upper()
        else:
            lst[i] = lst[i].lower()
        start += 1
        if lst[i]== ' ':
            start = 0
        answer += lst[i]
    return answer
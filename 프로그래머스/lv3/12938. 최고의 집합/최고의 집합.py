def solution(n, s):
    if n == 1:
        return [s]
    if n > s:
        return [-1]
    answer = [s//n for _ in range(n)]
    idx = len(answer) - 1
    for _ in range(s%n):
        answer[idx] += 1
        idx -= 1
    return answer
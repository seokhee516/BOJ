def solution(m, n, x, y, balls):
    answer = []
    for a, b in balls:
        tmp = []
        if x != a or y > b:
            tmp.append(abs(x-a)**2 + abs(2*n-y-b)**2)
        if x != a or y < b:
            tmp.append(abs(x-a)**2 + abs(y+b)**2)
        if y != b or x < a:
            tmp.append(abs(x+a)**2 + abs(y-b)**2)
        if y != b or x > a:
            tmp.append(abs(2*m-x-a)**2 + abs(y-b)**2)
        answer.append(min(tmp))
    return answer
def solution(e, starts):
    divisors = [0] * (e+1)
    checker = [0] * (e+1)
    
    for i in range(1, e+1):
        for j in range(i, e+1):
            if (temp:=i*j) > e:
                break
            if i == j:
                divisors[temp] += 1
            else:
                divisors[temp] += 2
    max_num = 0
    for idx in range(e, 0, -1):
        if divisors[idx] >= max_num:
            max_num = divisors[idx]
            checker[idx] = idx
        else:
            checker[idx] = checker[idx+1]
    return [checker[start] for start in starts]
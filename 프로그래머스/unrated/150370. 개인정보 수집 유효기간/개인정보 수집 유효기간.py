def solution(today, terms, privacies):
    answer = []
    d = {}
    for t in terms:
        k, v = t.split()
        d[k]=int(v)
    tmp = today.split(".")
    today_year, today_month, today_day = tmp[0],tmp[1], tmp[2]
    for i, p in enumerate(privacies):
        tmp = p.split()
        date, op = tmp[0],tmp[1]
        tmp = date.split(".")
        p_year, p_month, p_day = tmp[0],tmp[1], tmp[2]
        sum_date = (int(today_year)-int(p_year))*12*28+(int(today_month)-int(p_month))*28+(int(today_day)-int(p_day))
        # print(sum_date)
        # sum_date = -sum_date
        # print(d[op]*28)
        if d[op]*28 <= sum_date:
            answer.append(i+1)
        
    return answer
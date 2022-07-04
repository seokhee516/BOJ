from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        d = {}
        for o in orders:
            for combi in list(combinations(o,c)):
                combi_string = "".join(sorted(combi))
                d[combi_string] = d.get(combi_string, 0) + 1
        if d:
            max_val = max(d.values())
            if max_val >= 2:
                for k, v in d.items():
                    if v == max_val:
                        answer.append("".join(k))
    answer.sort()
    return answer
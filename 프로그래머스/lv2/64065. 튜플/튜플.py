def solution(s):
    s = s.replace('{','').replace('}','')
    lst = s.split(',')
    d = {}
    for i in lst:
        d[int(i)] = d.get(int(i),0) +1
    d = sorted(d.items(),reverse=True, key=lambda x:x[1])
    answer = [t[0] for t in d]
    return answer
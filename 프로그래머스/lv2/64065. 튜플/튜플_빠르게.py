from collections import Counter
def solution(s):
    s = s.replace('{','').replace('}','')
    lst = s.split(',')
    d = Counter(lst)
    d = sorted(d.items(),reverse=True, key=lambda x:x[1])
    answer = [int(t[0]) for t in d]
    return answer

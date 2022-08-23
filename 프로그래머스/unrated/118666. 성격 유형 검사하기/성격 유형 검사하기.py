from collections import defaultdict
def solution(survey, choices):
    answer = ''
    
    d = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] < 4:
            d[survey[i][0]] += (4-choices[i])
        else:
            d[survey[i][1]] += (choices[i]-4)
    category = [('R','T'),('C','F'),('J','M'),('A','N')]
    for c in category:
        if d[c[0]] >= d[c[1]]:
            answer += c[0]
        else:
            answer += c[1]
    return answer
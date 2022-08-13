from collections import defaultdict
def solution(records):
    name = defaultdict(str)
    inout = defaultdict(tuple)
    cnt = 0
    for record in records:
        data = record.split()
        if data[0] == 'Enter':
            name[data[1]] = data[2]
            inout[cnt] = (data[1],True)
            cnt += 1
        if data[0] == 'Leave':
            inout[cnt] = (data[1],False)
            cnt += 1
        if data[0] == 'Change':
            name[data[1]] = data[2]
    ans = []
    for i in range(len(inout)):
        ret = inout[i]
        if ret[1]:
            ans.append(name[ret[0]]+"님이 들어왔습니다.")
        else:
            ans.append(name[ret[0]]+"님이 나갔습니다.")
    return ans
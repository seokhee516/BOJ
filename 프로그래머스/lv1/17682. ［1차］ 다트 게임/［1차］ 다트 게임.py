def solution(dart):
    tmp = []
    i = 0
    while i < len(dart):
        if dart[i] == '*':
            tmp[-1] *= 2
            if len(tmp) > 1:
                tmp[-2] *= 2
        elif dart[i] == '#':
            tmp[-1] *= -1
        elif dart[i].isdigit():
            if dart[i] == '1' and len(dart) > i+1 and dart[i+1] == '0':
                tmp.append(10)
                i += 1
            else:
                tmp.append(int(dart[i]))
        elif dart[i].isalpha:
            if dart[i] == 'S':
                tmp[-1] **= 1
            elif dart[i] == 'D':
                tmp[-1] **= 2
            elif dart[i] == 'T':
                tmp[-1] **= 3
        i += 1
        # print(tmp)
    return sum(tmp)
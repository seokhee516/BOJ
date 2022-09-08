# 2차원 평면상의 좌표를 2차원 배열의 좌표로 찍어내려면 
# x, y = abs(max_y-y) , abs(min_x-x)
# from itertools import combinations
def solution(line):
    # max_x, max_y = 0, 0
    # min_x, min_y = 1e9, 1e9
    star = []
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            t1 = line[i]
            t2 = line[j]
            a, b, e = t1[0], t1[1], t1[2]
            c, d, f = t2[0], t2[1], t2[2]
            if (a*d - b*c) == 0:
                continue
            x = (b*f - e*d)/(a*d - b*c)
            y = (e*c - a*f)/(a*d - b*c)
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                if (x,y) not in star:
                    star.append((x,y))
                    # max_x = max(x, max_x)
                    # max_y = max(y, max_y)
                    # min_x = min(x, min_x)
                    # min_y = min(y, min_y)
    max_x, min_x = max(star)[0], min(star)[0]
    max_y, min_y = max(star, key=lambda x:x[1])[1], min(star, key=lambda x:x[1])[1]
    ans = [['.']*(abs(max_x-min_x)+1) for _ in range(abs(max_y-min_y)+1)]
    for x,y in star:
        x, y = abs(max_y-y) , abs(min_x-x)
        ans[x][y] = "*"
    for i,v in enumerate(ans):
        ans[i] = ''.join(v)
    return ans
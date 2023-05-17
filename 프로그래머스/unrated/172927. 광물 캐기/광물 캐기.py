from collections import deque
def solution(picks, minerals):
    answer = 0
    val = {0:{"diamond":1, "iron":1, "stone":1}, 1:{"diamond":5, "iron":1, "stone":1}, 2:{"diamond":25, "iron":5, "stone":1}}
    info = []
    q = deque(minerals[:5 * sum(picks)])
    while q:
        cnt = 0
        dia, iron, stone = 0,0,0
        while cnt < 5:
            cnt += 1
            mineral = q.popleft()
            # print(mineral)
            dia += val[0][mineral]
            iron += val[1][mineral]
            stone += val[2][mineral]
            if not q:
                break
        info.append([dia,iron,stone])
        # print([dia,iron,stone])
    info.sort(key = lambda x : [x[2],x[1],x[0]])
    # print(info)
    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer

    return answer
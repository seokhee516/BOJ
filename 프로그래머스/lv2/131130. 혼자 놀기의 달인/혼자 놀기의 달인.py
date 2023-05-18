def solution(cards):
    box = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] -1
        box.append([] if sorted(tmp) in box else sorted(tmp))
    box.sort(key=len)
    return len(box[-1]) * len(box[-2])
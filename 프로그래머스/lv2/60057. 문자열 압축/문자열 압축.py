def solution(s):
    answer = 0
    res = []
    for i in range(1, len(s)+1):
        word = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s)+i, i):
            # print(tmp, s[j:i+j], cnt, i, j, word)
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    word = word + str(cnt) + tmp
                else:
                    word = word + tmp
                tmp = s[j:j+i]
                cnt = 1
        # print(word)
        res.append(len(word))
    return min(res)
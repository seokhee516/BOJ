from itertools import permutations
import copy
def solution(expression):
    ans = 0
    expression_split = []
    j = 0
    for i in range(len(expression)):
        if "*" == expression[i] or "+" == expression[i] or "-" == expression[i]:
            expression_split.append(expression[j:i])
            expression_split.append(expression[i])
            j = i+1
    expression_split.append(expression[j:])

    operation = list(permutations(['*','+','-'],3))
    for o in operation:
        tmp = copy.deepcopy(expression_split)
        for i in range(2):
            c = 0
            while o[i] in tmp[c:]:
                idx = tmp.index(o[i])
                tmp = tmp[:idx-1] + [str(eval("".join(tmp[idx-1:idx+2])))] + tmp[idx+2:]
                c = idx-1
        ans = max(ans, abs(eval("".join(tmp))))
    return ans
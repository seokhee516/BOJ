import re
from itertools import combinations
def solution(str1, str2):
    # 소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()
    # 두글자 끊기 특수문자, 숫자 제거
    set1 = []
    for i in range(len(str1)-1):
        tmp = re.sub(r"[^a-z]","",str1[i:i+2])
        if len(tmp) == 2:
            set1.append(tmp)
    set2 = []
    for i in range(len(str2)-1):
        tmp = re.sub(r"[^a-z]","",str2[i:i+2])
        if len(tmp) == 2:
            set2.append(tmp)
    inter = [] # 교집합
    for i in set1:
        if i in set2:
            set2.remove(i)
            inter.append(i)
    union = set1+set2 # 합집합
    if len(union) == len(inter):
        j = 1
    elif len(union) == 0:
        j = len(inter)
    else:
        j = len(inter) / len(union)
    return int(j * 65536)
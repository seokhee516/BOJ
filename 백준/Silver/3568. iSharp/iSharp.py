import sys
input = sys.stdin.readline

data = input().strip().split()

base = data[0]
data = data[1:]
for d in data:
    d = d.replace(',','').replace(';','')
    print(base, end = '') # 기본 변수형

    for i in range(len(d)-1, 0, -1): # 변수 오른쪽에서 왼쪽으로
        if not d[i].isalpha():
            if d[i] == ']':
                print('[', end='')
            elif d[i] == '[':
                print(']', end='')
            else:
                print(d[i], end='')

    print(' ', end = '') # 변수 사이 공백

    for i in range(len(d)): # 알파벳
        if d[i].isalpha():
            print(d[i], end='')

    print(';') # 마무리
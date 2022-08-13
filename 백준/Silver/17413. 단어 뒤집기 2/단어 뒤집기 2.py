import sys
input = sys.stdin.readline
data = list(input().strip())
i = 0
s = 0
n = len(data)
while i < n:
    if data[i] == '<': # 괄호를 만나면
        i += 1
        while data[i] != '>': # 괄호가 끝날때까지
            i += 1
        i += 1
    elif data[i].isalnum(): # 숫자나 알파벳을 만나면
        s = i
        while i < n and data[i].isalnum():
            i += 1
        tmp = data[s:i] # 뒤집어서 넣어주기
        tmp.reverse()
        data[s:i] = tmp
    else: # 공백을 만나면
        i += 1 # 지나가기

print(''.join(data))
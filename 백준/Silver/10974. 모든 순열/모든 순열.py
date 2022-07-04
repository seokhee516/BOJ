import sys
input = sys.stdin.readline
n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp) # 이쁘개 출력됨
        return
    for i in range(1, n + 1):
        if i not in temp: # 1부터 n까지 없는거 넣어줌
            temp.append(i)
            dfs()
            temp.pop()

dfs()
'''
4
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
'''
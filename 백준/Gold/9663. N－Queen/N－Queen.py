# 백트래킹은 봐도 봐도 어렵당... 다들 어케푸는거냐~
import sys
input = sys.stdin.readline
n = int(input())
ans = 0
row = [0] * n # 1차원 배열의 인덱스와 값을 통해 위치 기록
# row[i] = j -> 퀸을 [i,j] 위치에 놓겠다
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i): # 다른 퀸이 같은 열에 있거나 대각선에 있는 경우
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

'''
만약에 현재 퀸을 놓은 위치가 (3, 3)라고 가정하면, 왼쪽 대각선의 좌표는 각각 (2, 2), (1, 1), (0, 0)이 된다.
여기서, (3, 3)을 i와 j라고 하고, (2, 2)를 x1, y1, (1, 1)을 x2, y2, (0, 0)을 x3, y3이라고 해보자.
i에서 x1을 뺀 값과 j에서 y1를 뺀 값은 모두 1로 같다.
또한, i에서 x2를 뺀 값과 j에서 y2를 뺀 값은 모두 2로 같다.
세 번째 경우도 3으로 마찬가지로 동일하다.
'''
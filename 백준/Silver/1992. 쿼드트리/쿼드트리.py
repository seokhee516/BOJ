import sys
input = sys.stdin.readline
n = int(input())
tree = [list(map(int, input().strip())) for _ in range(n)]
res = []

def quad_tree(x,y,n):
    global res
    color = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: # 색이 다른 경우 4분면으로 나누기
                res.append("(") # 4분면 나눌 때 괄호 추가
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                res.append(")")
                return
    res.append(color)

quad_tree(0,0,n)
print("".join(map(str, res)))
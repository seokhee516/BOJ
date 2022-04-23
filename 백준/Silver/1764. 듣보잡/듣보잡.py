import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 집합
de = {input().strip() for _ in range(n)}
bo = {input().strip() for _ in range(m)}
# 교집합 중복되는 분자열 선택 후, 정렬
debo = sorted((de & bo))

print(len(debo))
for db in debo:
    print(db)
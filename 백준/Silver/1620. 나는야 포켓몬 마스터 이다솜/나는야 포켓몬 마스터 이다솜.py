import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pokelist = []
pokedict = {}
for i in range(n):
    poke = input().strip()
    pokelist.append(poke)
    pokedict[poke] = i + 1
for _ in range(m):
    q = input().strip()
    '''
    isdigit() 숫자로만 이뤄져 있는지 확인하는 함수
    '''
    if q.isdigit():
        print(pokelist[int(q)-1])
    else:
        print(pokedict[q])
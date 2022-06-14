import sys
input = sys.stdin.readline
from collections import deque
length = int(input())
# 튜플 형태로 넣기 (풍선의 번호, 종이에 적힌 번호)
# deque([(1, -5), (2, -5), (3, -5), (4, -5), (5, -5)])
arr = [i for i in range(1, length+1)]
arr = deque(zip(arr, map(int, input().split()))) 

ans = []
while arr:
    num, paper_num = arr.popleft()
    ans.append(num)
    if paper_num > 0:
        arr.rotate(-(paper_num-1))
    else:
        arr.rotate(-paper_num)
print(' '.join(map(str, ans)))
# rotate를 활용하자!! 양수일때 시계방향, 음수일때 반시계 방향
'''
비슷한 로직인데 내 풀이는 왜 시간초과 뜨지?
나는 while을 통해 물어보고 빼서(pop) 넣고(append) 과정이 반복되서 느려진것 같다...
그리고 양수 음수 조건을 따로 썼는데 그냥 양수일때 -1해주니까 같네
ans = []
while length > 1:
    num, paper_num = arr.popleft()
    ans.append(num)
    length -= 1
    if length == 1:
        break
    if paper_num > 0:
        paper_num %= length
        while paper_num !=1:
            arr.append(arr.popleft())
            paper_num -= 1
    else:
        paper_num = -(abs(paper_num)%length)
        while paper_num != 0:
            arr.insert(0,arr.pop())
            paper_num += 1
ans.append(arr.pop()[0])
for a in ans:
    print(str(a), end = ' ')
'''
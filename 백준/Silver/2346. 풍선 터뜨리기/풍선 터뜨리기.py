import sys
input = sys.stdin.readline
from collections import deque
length = int(input())
arr = [i for i in range(1, length+1)]
arr = deque(zip(arr, map(int, input().split()))) 

ans = []
while arr:
    num, paper_num = arr.popleft() # 풍선의 번호, 종이에 적힌 번호
    ans.append(num)
    if paper_num > 0: # 양수일 경우
        arr.rotate(-(paper_num-1)) # 시계 반대로
    else: # 음수일 경우
        arr.rotate(-paper_num) # 시계방향
print(' '.join(map(str, ans)))
'''
비슷한 로직인데 내 풀이는 시간초과 떴당..ㅠ
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


결론!! rotate를 활용하자!! 양수일때 시계방향, 음수일때 반시계 방향


추가 1) arr 길이 보다 paper_num 이 크거나 작을때 나머지 수로 줄여줄려했는데 
크기가 1000개 미만이어서 시간 차이는 없었당
while arr:
    num, paper_num = arr.popleft()
    ans.append(num)
    length -= 1
    if length == 0:
        break
    if paper_num > 0:
        paper_num %= length
        arr.rotate(-(paper_num-1))
    else:
        paper_num = -(abs(paper_num)%length)
        arr.rotate(-paper_num)

추가 2) 튜플 형태로 입력 받기
q = deque(enumerate(map(int, input().split())))
enumerate 사용 전
deque([3, 2, 1, -3, -1])
enumerate 사용 후
deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

나는 리스트를 하나 만들어서 zip으로 추가하는 방식이었는데 
enumerate를 사용하면 index를 튜플 형태로 바로 저장할 수 있당 대박쓰~
'''

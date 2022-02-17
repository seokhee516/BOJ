import sys
input = sys.stdin.readline # 
t = int(input()) # int 사용할 때 strip() 필요 없음
# 컨트롤 시프트 알 : 리팩토링 함수로 만들기
def new_func(n, phone_book):
    for k in range(n-1):
        if phone_book[k+1].startswith(phone_book[k]): # 아스키순으로 들어오므로 바로 뒤만 비교
            return "NO\n" # 뒤에 있으면 함수 끝남 
    return "YES\n" # 없으면 YES,  sys.stdout.write 받기 위해 \n 추가

for _ in range(t):
    n = int(input())
    phone_book = [input().strip() for _ in range(n)] # 리스트 컴프리헨션 빠름, input str로 받음
    phone_book.sort() # 아스키순 nlogn
    answer = new_func(n, phone_book)
    sys.stdout.write(answer) # print 대신 빠르게 출력
   
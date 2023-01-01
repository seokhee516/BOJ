N = int(input())
answers = []

def get_decrease(num) :
    answers.append(num)

    peak = int(str(num)[0])
    for i in range(peak + 1, 10) :
        get_decrease(int(str(i) + str(num)))

for i in range(10):
    get_decrease(i)

answers.sort()
try :
    print(answers[N])
except : 
    print(-1)
    
    

'''
재귀함수를 호출하여 큰 값을 앞에다 붙이는 방식
line 11 0 부터 9까지 탐색
line 8 재귀함수 내부에 들어온 숫자의 맨 처음 값 20->2 + 1 부터 10까지 탐색 
line 9 입력받은 숫자보다 항상 커야 하므로 str(i)+str(num) 형태로 재귀 호출
answers sort 전
[0, 10, 210, 3210, 43210, 543210, 6543210, 76543210, 876543210, 
9876543210, 976543210, 86543210, 986543210, 96543210, 7543210, 87543210, 
987543210, 97543210, 8543210, 98543210, 9543210, 643210, 7643210, 87643210, 
987643210, 97643210, 8643210, 98643210, 9643210, 743210, 8743210, 98743210, 9743210, 843210,...
'''
import sys
input = sys.stdin.readline
target = int(input())
# 채널 100에서 시작
ans = abs(100-target)
m = int(input())
# m이 존재할 때만
if m:
    button = list(map(str, input()))
else:
    button = []
'''
나는 사용할 수 있는 버튼을 리스트화해서 이를 이용해 가까운 수를 구할려했다...
하지만 모든 수를 세어가면서 가까운 수를 저장하는 방법이 있었다..!! 이것이 부르트포스구나~
'''
# 1000001로 설정하는 이유는 채널의 수가 0 ≤ N ≤ 500,000 이므로 
# 작은 수에서 큰수로 이동하는 경우와 큰수에서 작은 수로 이동하는 경우를 범위에 포함시키는 것이다
for num in range(1000001):
    # 숫자를 한자리씩 비교하여
    for n in str(num):
        # 고장난 버튼을 포함할때 멈춘다
        if n in button:
            break
    # for -else 문
    else:
        ans = min(ans, len(str(num))+abs(num-target))
print(ans)
'''
for-else문 이라는게 있었다!
파이썬은 for과 while 문에 else를 같은 줄에 놓을 수 있다.
반복문 도중 break가 되지 않고 끝까지 반복을 실행했을 경우 else에 있는 코드를 실행하게 하는 것이다.

보통 반복문을 사용할 때 반복문 내에 break를 두는 경우가 많은데, 
break로 인해 반복문을 빠져나왔는지, 반복문 조건이 멈춰서 빠져나왔는지 알 수 없는 경우가 많다.
그래서 flag 등을 둬서 처리하는데 for -else를 쓰면 그럴 필요가 없다.

위 문제의 경우 고장난 버튼을 포함하여 break 되었을때 ans를 저장하는 것이 아니라, 
고장난 버튼 없이 끝까지 실행된 경우만 ans를 저장하게 된다.
'''
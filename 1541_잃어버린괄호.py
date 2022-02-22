import sys
input = sys.stdin.readline
test = input().strip().split('-') #마이너스를 기준으로 나누기. '-' 없어도 split 가능 리스트로 만들어짐
ans = 0
for i in test[0].split('+'): # 가장 앞에 수. '+' 있으나 없으나 가능
    ans += int(i) # 값에 더하기
# 마이너스 기준으로 더해서 큰값으로 만든 후, 빼줌
for i in test[1:]:
    for j in i.split('+'): # '+' 있으나 없으나 가능
        ans -= int(j) # 빼기
print(ans)
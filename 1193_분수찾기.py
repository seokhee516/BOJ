import sys
n = int(sys.stdin.readline())
line = 0 # 몇번째 줄
end = 0 # 마지막 값 인덱스
while n > end:
    line += 1
    end += line 

diff = end - n # 마지막과 n의 차이
if line % 2 != 0: # 홀수 줄일때
    top = diff + 1 # 분자 감소
    bottom = line - diff # 분모 증가
else: # 짝수 줄일 때
    top = line - diff # 분자 증가 
    bottom = diff + 1 # 분모 감소

print(f"{top}/{bottom}")
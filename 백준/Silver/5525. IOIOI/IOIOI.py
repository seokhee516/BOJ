import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().strip()

# 정답
ans = 0
# 연속된 횟수
cnt = 0 
# 시작점 
start = 0

# p의 최소 길이 만큼 확인할 수 있을때까지
while start < m-2:
    # 시작점에 IOI 있으면
    if s[start:start+3] == 'IOI':
        # 시작점 2칸 이동 (IO이므로)
        start += 2
        # 연속된 횟수 한번 추가
        cnt += 1
        # 연속된 횟수가 n과 같으면
        if cnt == n:
            # 정답에 1 추가
            ans += 1
            # 뒤에 연속으로 또 있을 수 있으므로 연속된 횟수 1 감소
            cnt -= 1
    # IOI 없다면
    else:
        # 시작점 1칸 이동 (한칸씩 확인하기 위해)
        start += 1
        # 연속된 횟수 초기화
        cnt = 0
print(ans)
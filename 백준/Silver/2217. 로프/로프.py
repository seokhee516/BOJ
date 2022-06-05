import sys
input = sys.stdin.readline

n = int(input())
# 로프 데이터 입력
data = [int(input()) for _ in range(n)]
# 로프의 중량 내림차순 정렬
data.sort(reverse=True)

result = []
for i in range(n):
    # 내림차순 정렬이므로 가장 큰수는 한개 그다음 수는 두개... 이런식
    # 로프가 큰지 작은지 한번 더 for 문으로 확인할 필요 없음, 모든 로프를 사용할 필요 없다는 조건도 만족
    result.append(data[i]* (i+1))


# 로프 중에 최대 중량 뽑기
print(max(result))
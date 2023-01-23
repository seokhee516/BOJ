import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def count_number(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

five_num = count_number(N, 5) - count_number(M, 5) - count_number(N-M, 5)
two_num = count_number(N, 2) - count_number(M, 2) - count_number(N-M, 2)
ans = min(five_num, two_num)
print(ans)

'''
끝자리가 0이라는 것은 10의 배수
10은 2와 5로 구성되어 있음 
line 6~11 nCr = n!/(n-r)!r!
line 13 5의 지수 = n!의 5의 지수 - r!의 5의 지수 - (n-r)!의 5의 지수
line 14 2의 지수 = n!의 2의 지수 - r!의 2의 지수 - (n-r)!의 2의 지수
line 15 2와 5의 짝이 맞아야 10이 되므로 2와 5의 개수 중 더 작은게 10의 개수 
'''
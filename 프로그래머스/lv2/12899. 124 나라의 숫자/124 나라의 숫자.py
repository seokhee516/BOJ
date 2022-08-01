# 3진법 활용해서 푼다
'''
n=1이면, n-1(1-1=0)을 해서 n%3(0%3=0)을 해서 1 출력
n=2이면, n-1(2-1=1)을 해서 n%3(1%3=1)을 해서 2 출력
n=3이면, n-1(3-1=2)을 해서 n%3(2%3=2)을 해서 4 출력
n=4이면, n-1(4-1=3)을 해서 n%3(3%3=0)을 해서 1 출력 -> n//3을 해서 1로 만들어주고 다시 n-1해서 0으로
n=5, 
n-1(5-1=4)을 해서 n%3(4%3=1)을 해서 2 출력
n//3(4//3=1)을 해서 n-1(1-1=0)을 해서 1출력 => '2'+'1' -> 반대로 출력
'''
def solution(n):
    ans = ""
    arr = ['1','2','4']
    while n > 0:
        n -= 1
        ans = arr[n%3] + ans # 반대로 출력
        n //=3
        
    return ans
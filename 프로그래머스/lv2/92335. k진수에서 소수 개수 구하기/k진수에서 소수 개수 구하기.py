def solution(n, k):
    answer = 0
    def solution(n, q):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)
        return rev_base[::-1] 
    lst = solution(n, k).split('0')
    def isPrime(a):
        if (a<2):
            return False
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True
    
    for l in lst:
        if l and isPrime(int(l)):
            answer += 1 
        
    return answer
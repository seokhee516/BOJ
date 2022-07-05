def solution(p):
    def isBalance(w):
        if w == "": # 빈 문자열인 경우, 빈 문자열을 반환
            return ""
        # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
        balance = 1
        for i in range(1, len(w)):
            if w[0] != w[i]:
                balance -= 1
            else:
                balance += 1
            i += 1
            if balance <= 0:
                break
        u = w[:i]
        v = w[i:]
        if isTrue(u): # u가 "올바른 괄호 문자열" 이라면 문자열
            u += isBalance(v) # v에 대해 1단계부터 다시 수행, 결과 문자열을 u에 이어 붙인 후 반환
            return u
        else: # u가 "올바른 괄호 문자열"이 아니라면
            e = "(" + isBalance(v) + ")" # '(' + 1단계 수행한 v + ')'
            u = u[1:-1] # u의 첫 번째와 마지막 문자를 제거
            u = e + change(u) # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
            return u # 생성된 문자열 반환
    def isTrue(u): # 올바른 괄호 문자열 확인 함수
        check = 0
        for i in range(len(u)):
            if u[i] == '(':
                check += 1
            else:
                check -= 1
            if check < 0:
                return False
        return True
    def change(st): # 괄호 방향 뒤집는 함수
        ret = []
        for s in st:
            if s == "(":
                ret.append(")")
            elif s == ")":
                ret.append("(")
        return "".join(ret)
    return isBalance(p)

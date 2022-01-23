'''
1. 정규표현식을 사용해봅시다. 조건에 맞춰 각각의 빈칸을 채워보세요.

import re
p = re.compile("ca.e")
m = p.match("case") 

# 조건 : "ca.e"와 매치된 문자열을 돌려준다.
print(빈칸) 

# 조건 : 매치된 문자열의 시작 위치를 돌려준다.
print(빈칸) 

# 조건 : 매치된 문자열의 끝 위치를 돌려준다.
print(빈칸) 

# 조건 : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
print(빈칸) 


( 힌트  : https://wikidocs.net/4308 이 사이트를 참고하세요)

2. 다음 문자열을 rjust 또는 zfill을 사용하여 출력하세요.
"119"
"00700"
"ss501"
'''
print("9".rjust(3,"1"))
print("700".zfill(5))
print("501".rjust(5,"s"))

import re
p = re.compile("ca.e")
m = p.match("case") 
print(m.group())
print(m.start())
print(m.end())
print(m.span())

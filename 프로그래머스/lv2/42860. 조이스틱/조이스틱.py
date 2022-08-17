def solution(name):
    ans = 0
    n = len(name)
    # 미리 위 아래 세어서 더해놓기
    move = [min(ord(c)-65, 91 - ord(c)) for c in name]
    ans += sum(move)
    # 쭉 가는 경우
    min_move = n -1
    
    for i, c in enumerate(name):
        next_i = i+1
        # A가 존재 하면 
        while next_i < n and name[next_i] == 'A':
            # A가 연속으로 몇개 있는지 확인
            next_i += 1
        min_move = min(min_move, (2*i)+(n-next_i), (2*(n-next_i)+i)) # 쭉탐색/오른쪽갔다가왼쪽/왼쪽갔다가오른쪽
    ans += min_move
    return ans
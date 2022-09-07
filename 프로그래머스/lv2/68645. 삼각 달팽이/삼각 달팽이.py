def solution(n):
    tri = [[0 for _ in range(i+1)] for i in range(n)] # 삼각형 만들기
    x, y = -1,0 # 처음 방향은 하이므로 x 미리 설정
    num = 1 # 채워넣을 수
    for k in range(n): # 방향 설정
        for _ in range(k, n): # 방향이 바뀔 때 하나씩 줄여나감
            if k % 3 == 0: # 하
                x += 1
            elif k % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            tri[x][y] = num
            num += 1
    ans = sum(tri,[]) # 여러겹의 리스트 하나로 합치기
    return ans
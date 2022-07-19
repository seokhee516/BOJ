

def solution(places):
    def distance_check(place,x, y):
        dx = [1,0,0,-1]
        dy = [0,-1,1,-0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] == 'P':
                    return True
                elif place[nx][ny] == 'X':
                    continue
                elif place[nx][ny] == 'O':
                    for j in range(4):
                        px = nx + dx[j]
                        py = ny + dy[j]
                        if dx[i] == dx[3-j] and dy[i] == dy[3-j]:
                            continue
                        if 0 <= px < 5 and 0 <= py < 5:
                            if place[px][py] == 'P':
                                return True
        return False
    def func(place, k):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if distance_check(place,i,j):
                        return 0
        return 1
    answer = [0] * 5
    for k in range(5):
        answer[k] = func(places[k], k)
    return answer
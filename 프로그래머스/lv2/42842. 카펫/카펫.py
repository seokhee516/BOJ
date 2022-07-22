def solution(brown, yellow):
    for i in range(1,yellow+1): # i는 세로길이
        if yellow % i != 0:
            continue
        j = yellow // i # j는 가로길이
        if (i*2)+(j*2)+4 == brown:
            answer = [j+2,i+2]
            break
    return answer
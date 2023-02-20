def solution(m, musicinfos):
    answer = '(None)'
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    max_time = 0
    for musicinfo in musicinfos:
        tmp = musicinfo.split(',')
        s_t,e_t,x,y = tmp[0],tmp[1],tmp[2],tmp[3]
        time = (int(e_t.split(':')[0])-int(s_t.split(':')[0]))*60 + (int(e_t.split(':')[1])-int(s_t.split(':')[1]))
        # print(time, len(y), time//len(y), time%len(y))
        y = y.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        z =''
        if time < len(y):
            z += y[:time]
        else:
            z += (y*(time//len(y)) + y[:time%len(y)+1])
        
        # print(z)
        if m in z:

            if time > max_time:
                max_time = time
                answer = x
    
    return answer

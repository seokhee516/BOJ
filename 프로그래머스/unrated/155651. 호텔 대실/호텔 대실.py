from collections import deque
def solution(book_times):
    answer = 0
    book_times.sort()
    print(book_times)
    
    tmp = book_times[0]
    book_times = book_times[1:]
    h, m = map(int, tmp[0].split(':'))
    cur = 60*h+m
    h, m = map(int, tmp[1].split(':'))
    e = 60*h+m+10
    room = [e]
    
    for book_time in book_times:
        h, m = map(int, book_time[0].split(':'))
        cur = 60*h+m
        h, m = map(int, book_time[1].split(':'))
        e = 60*h+m+10
        room.sort()
        if cur >= room[0]:
            room.pop(0)
        room.append(e)
    answer = len(room)
    return answer
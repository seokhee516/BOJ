def solution(book_times):
    book_times.sort()
    room = [0]
    for book_time in book_times:
        h, m = map(int, book_time[0].split(':'))
        cur = 60*h+m
        h, m = map(int, book_time[1].split(':'))
        e = 60*h+m+10
        room.sort()
        if cur >= room[0]:
            room.pop(0)
        room.append(e)
    return len(room)
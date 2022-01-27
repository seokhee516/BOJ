'''
def consecutive_sum(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)
print(consecutive_sum(1, 10))
'''
def merge(list1, list2):
    if list1 < list2:
        return list1.extend(list2)
    

print(merge([2],[1]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
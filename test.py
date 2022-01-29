'''
def consecutive_sum(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)
print(consecutive_sum(1, 10))
'''

'''
def merge(list1, list2):
    merged_list = []
    i = 0 
    j = 0 
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    if len(list1) == i:
        merged_list += list2[j:]
    elif len(list2) == j:
        merged_list += list1[i:]
    return merged_list

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    mid = len(my_list)//2
    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))


lst = [16, 11, 6, 13]
print(merge_sort(lst))
'''

def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    i = start
    b = start
    p = end
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, p)
    p = b
    return p

# 퀵 정렬
def quicksort(my_list, start, end):
    if (end-start) < 1:
        return

    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot-1)
    quicksort(my_list, pivot+1 ,end)


# 테스트 1
# list1 = [1, 4, 6, 7, 11, 16, 10, 13]
# list1 = [1, 4, 6]
# list1 = [11, 16, 10, 13]
# list1 = [11, 10, 13]
list1 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list1, 0, len(list1) - 1)
print(list1)


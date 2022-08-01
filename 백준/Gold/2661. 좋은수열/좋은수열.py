import sys
input = sys.stdin.readline
# 답 보고 풀었는데도 잘 모르겠당...ㅠㅠ
def back(result, arr_len):
    # 현재자릿수의 절반만큼 묶어서 나쁜 수열인지 체크
    for part_len in range(1, arr_len//2+1):
        if str(result)[arr_len-part_len:] == str(result)[arr_len-2*part_len:arr_len-part_len]:
            return
    if arr_len == N:
        print(result)
        exit(0)
    for i in range(1, 4):
        temp = result * 10 + i
        back(temp, arr_len+1)


N = int(input())
back(0, 0)

'''
1 		-> 좋은 수열
11		-> 나쁜 수열 마지막 수 1 증가
12		-> 좋은 수열
121		-> 좋은 수열
1211		-> 나쁜 수열 마지막 수 1 증가 part_len = 1 arr_len-part_len = 3
1212		-> 나쁜 수열 마지막 수 1 증가 part_len = 2 arr_len-part_len = 2
1213		-> 좋은 수열
12131		-> 좋은 수열
121311		-> 나쁜 수열 마지막 수 1 증가
121312		-> 좋은 수열
1213121		-> 좋은 수열
'''
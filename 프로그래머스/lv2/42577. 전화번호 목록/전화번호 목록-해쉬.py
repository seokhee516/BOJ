# 해쉬로 풀기
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_num in phone_book:
        # 존재하는 경우 해쉬맵에 1로 넣기
        hash_map[phone_num] = 1
    for phone_num in phone_book:
        temp = ""
        # 접두어니까 앞에서부터 한글자씩 확인 (전화번호 최대 길이 20)
        for number in phone_num:
            temp += number
            # 접두어 해쉬맵에 있고, 전화번호랑 같은 값이 아니라면
            if temp in hash_map and temp != phone_num:
                answer = True 
    return answer

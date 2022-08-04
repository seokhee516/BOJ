def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        time = 0
        price = prices[i]
        for j in range(i+1, len(prices)):
            time += 1
            if price > prices[j]:
                break
        answer[i] = time
    return answer
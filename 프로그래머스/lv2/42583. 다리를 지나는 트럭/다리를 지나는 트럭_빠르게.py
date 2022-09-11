from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0 # 다리를 건너는 시간
    bridge = deque([0]) * bridge_length # 빈 다리 만들기
    total_weight =0
    truck_weights.reverse() # 시간 줄이기 위해 리버스
    while truck_weights: # 트럭이 다 지나는 동안
        ans += 1
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] <= weight: # 다리 위 트럭의 무게가 최대무게보다 작거나 같을때
            truck = truck_weights.pop()
            bridge.append(truck) # 트럭 올려줌
            total_weight += truck
        else:
            bridge.append(0) # 아니면 지나가기
    ans += bridge_length # 제일 마지막에 들어온게 나가는 시간    
    return ans

# from collections import deque
def solution(bridge_length, weight, truck_weights):
    # truck_weights = deque(truck_weights) # 큐로 바꾸기
    ans = 0 # 다리를 건너는 시간
    bridge = [0] * bridge_length # 빈 다리 만들기
    while bridge:
        ans += 1
        bridge.pop(0)
        if truck_weights: # 트럭이 다 지나는 동안
            if sum(bridge) + truck_weights[0] <= weight: # 다리 위 트럭의 무게가 최대무게보다 작거나 같을때
                bridge.append(truck_weights.pop(0)) # 트럭 올려줌
            else:
                bridge.append(0) # 아니면 지나가기
        
    return ans
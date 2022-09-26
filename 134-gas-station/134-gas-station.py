class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, surplus, start = 0, 0, 0 # tank: 전체 저장된 값 surplus: 현재 시점의 잉여 값 start: 시작값
        for i in range(len(gas)):
            tank += gas[i] - cost[i] 
            surplus += gas[i] - cost[i] 
            if surplus < 0: # 잉여값이 음수라면
                start = i+1 # 시작값을 현재값 다음으로 넘겨줌
                surplus = 0 # 잉여값 초기화
        if tank >= 0: # 남은 가스 있음! travel 가능
            return start # 
        else:
            return -1
'''
from collections import deque
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = deque(gas)
        cost = deque(cost)
        tank = 0

        for idx in range(len(gas)):
            if gas[0] - cost[0] < 0: 
                gas.append(gas.popleft())
                cost.append(cost.popleft())
            else:
                tank = gas[0]
                gas.append(gas.popleft())
                for i in range(len(gas)):
                    tank -= cost[i] 
                    if tank < 0: 
                        break
                    tank += gas[i]
                cost.append(cost.popleft())
            if tank > 0:
                return idx
            tank = 0
        return -1

쌩구현. n의 최대값이  10^5이므로 이중 for 문 돌리면 10^10 시간초과
cost 값보다 gas가 적으면 수행되지 않음 -> if surplus < 0 으로 확인 가능
surplus로 들어오는 값이 양수인지 계속 확인하므로 마지막에 tank > 0 이라면 무조건 답임
"If there exists a solution, it is guaranteed to be unique" 조건 있으므로 만족하는 start 값은 하나이므로 
tank가 0보다 크게 만드는 start값이 답임
'''
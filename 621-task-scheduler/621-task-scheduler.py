# input
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task 개수 세기
        task_count = sorted(Counter(tasks).items(), key = lambda x: x[1]) # [('B', 1), ('C', 1), ('D', 1), ('E', 1), ('F', 1), ('G', 1), ('A', 6)]
        # 가장 많이 등장한 task 뽑기
        max_task = task_count.pop()[1] # 6
        # 최대 idle 설정 
        idle = (max_task-1)*n # 10 A idle idle A idle idle A idle idle A idle idle A idle idle A
        # 그리디 수행 idle에 다른 task들을 채워준다고 생각하기
        for i in range(len(task_count)-1, -1, -1):
            # idle이 필요한 개수에서 채워준 task들의 수를 빼주기
            # max_task랑 같은 개수를 가지는 task가 있으면 max_task-1을 해줘야 하기 때문에 min함수를 씌워줌
            # A -> B -> idle -> A -> B -> idle -> A -> B 이런 경우
            idle -= min(task_count[i][1], max_task-1) # task_count[i][1]: 3, max_task-1: 2
            '''
            idle: 10, task_count[i][1]: 1, max_task-1: 5
            idle: 9, task_count[i][1]: 1, max_task-1: 5
            idle: 8, task_count[i][1]: 1, max_task-1: 5
            idle: 7, task_count[i][1]: 1, max_task-1: 5
            idle: 6, task_count[i][1]: 1, max_task-1: 5
            idle: 5, task_count[i][1]: 1, max_task-1: 5
            '''
        idle = max(0, idle) # 4
        return len(tasks) + idle # 원래 길이 + idle 개수
# output 16
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

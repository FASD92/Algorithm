"""
기존 코드
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr_weight = 0
    timer = 0
    waiting_trucks = deque(truck_weights)
    distances = deque([False] * len(truck_weights))
    
    while waiting_trucks:
        for i in waiting_trucks:    # 대기 버스 리스트를 순회하며
            if not distances[i] and (curr_weight + waiting trucks[i]) <= weight:    # 만약 해당 버스가 아직 대기중이고 다리에 올라갔을 때 다리 부하가 weight보다 작거나 같으면, 
                distances[i] += 1   # 해당 버스의 주행 거리에 1을 추가한다(즉, 다리에 올린다.)
                timer += 1  # 시간을 경과시킨다.
        if distances[0] > bridge_length:  # 맨 앞 버스의 주행거리가 다리의 길이를 넘어가면, 즉 다리를 건너면
            distance.popleft()
            waiting_trucks.popleft()    # 대기 버스에서 제거한다.
"""


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    curr_weight = 0
    
    while bridge:
        answer += 1
        
        exited = bridge.popleft()
        curr_weight -= exited
        
        if waiting:
            if curr_weight + waiting[0] <= weight:
                new_truck = waiting.popleft()
                bridge.append(new_truck)
                curr_weight += new_truck
            else:
                bridge.append(0)
    return answer
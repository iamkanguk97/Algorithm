from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = deque([0] * bridge_length)   # 다리 큐
    truck_weights = deque(truck_weights)   # 대기트럭 큐

    currentBridgeWeight = 0
    while truck_weights:
        second += 1
        currentBridgeWeight -= bridge.popleft()
        
        if currentBridgeWeight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()   # 대기트럭 큐에서 하나의 트럭 뺌
            bridge.append(truck)   # 다리 들어감
            currentBridgeWeight += truck
        else:
            bridge.append(0)
    
    second += bridge_length
    return second
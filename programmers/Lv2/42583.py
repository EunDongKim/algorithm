def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossover = []
    bridge = []
    waiting = []
    n = len(truck_weights)
    
    while n != len(crossover):
        

        # 다리를 건너는 트럭 => 다리를 지난 트럭
        if len(bridge) != 0 and sum(bridge) != 0:
            for i in range(len(waiting)):
                try :
                    print(waiting)
                    waiting[i] -= 1
                    if waiting[i] <= 0:
                        crossover.append(bridge.pop(0))
                        waiting.pop(0)
                except :
                    break

        # 다리를 못건넌 트럭 => 다리를 건너는 트럭
        if len(truck_weights) != 0 and (len(bridge) == 0 or (sum(bridge) + truck_weights[0] <= weight and len(bridge) < bridge_length)):
            bridge.append(truck_weights.pop(0))
            waiting.append(bridge_length)
        answer += 1
        print(answer, crossover, bridge, truck_weights)
    return answer
print(solution(2,10,[7,4,5,6]))

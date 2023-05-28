def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0 
    
    while progresses:
        if (progresses[0] + time*speeds[0]) >=100 :  # 하나의 기능 개발 완료 
            progresses.pop(0)
            speeds.pop(0)
            count +=1  # 넘어간 개발의 수 
            
        else : # 더 개발해야함 # 시간이 더 필요 
            if count > 0 : # 연속으로 넘어갈 기회를 놓침 
                answer.append(count) 
                count = 0
            time += 1
            
    answer.append(count)
    return answer
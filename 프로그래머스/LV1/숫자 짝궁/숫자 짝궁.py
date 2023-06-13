"""
프로그래머스 LV1: 숫자 짝궁 (휴.. 풀었다)
https://school.programmers.co.kr/learn/courses/30/lessons/131128
"""

def solution(X, Y):
    x_count, y_count = [0] * 10, [0] * 10
    
    # 숫자 몇번 나왔는지 저장
    for x in X:
        x_count[int(x)] += 1
    for y in Y:
        y_count[int(y)] += 1
        
    # print(x_count, y_count)
    
    result = ""
    for i in range(9, -1, -1):
        result += str(i) * min(x_count[i], y_count[i])
    
    if result == "":
        return "-1"
    else:
        zeroCheck = True
        for j in range(len(result)):
            if result[j] != '0':
                zeroCheck = False
                break
        if zeroCheck == True:
            return "0"
        return result
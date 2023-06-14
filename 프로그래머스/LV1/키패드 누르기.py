"""
프로그래머스 LV1: 키패드 누르기
https://school.programmers.co.kr/learn/courses/30/lessons/67256
2020년도 카카오 인턴십
"""

# 해당 번호 인덱스 구하는 함수
def getTargetIndex(keypad, target):
    find = False
    x, y = None, None
    
    for idx, kp in enumerate(keypad):
        for i in range(len(kp)):
            if kp[i] == target:
                find = True
                y = i
                break
        if find == True:
            x = idx
            break
    
    return (x, y)
    

# 손가락 정하는 함수
def selectFinger(keypad, left, right, target):
    target_point = getTargetIndex(keypad, target)   # target의 index 찾기
    left_d = abs(left[0] - target_point[0]) + abs(left[1] - target_point[1])
    right_d = abs(right[0] - target_point[0]) + abs(right[1] - target_point[1])
    
    if left_d == right_d:
        return ('S', target_point)
    else:
        return ('L', target_point) if left_d < right_d else ('R', target_point)


def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]   # 키패드
    left = [1, 4, 7]   # 왼쪽 손가락
    right = [3, 6, 9]   # 오른쪽 손가락
    
    result = ''
    left_thumb = (3, 0)   # 왼쪽 엄지손가락 시작위치
    right_thumb = (3, 2)   # 오른쪽 엄지손가락 시작위치
    for number in numbers:
        if number in left:   # 왼쪽 손가락만 갈 수 있는 번호면 바로 L 반환
            leftIdx = left.index(number)
            result += 'L'
            left_thumb = (leftIdx, 0)   # 손가락 이동
        elif number in right:   # 오른쪽 손가락만 갈 수 있는 번호면 바로 R 반환
            rightIdx = right.index(number)
            result += 'R'
            right_thumb = (rightIdx, 2)   # 손가락 이동
        else:
            selectResult = selectFinger(keypad, left_thumb, right_thumb, number)
            if selectResult[0] == 'S':
                if hand == 'right':
                    result += 'R'
                    right_thumb = selectResult[1]
                else:
                    result += 'L'
                    left_thumb = selectResult[1]
            elif selectResult[0] == 'L':
                result += 'L'
                left_thumb = selectResult[1]
            else:
                result += 'R'
                right_thumb = selectResult[1]
                
    return result
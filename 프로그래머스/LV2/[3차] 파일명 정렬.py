"""
프로그래머스 LV2: [3차] 파일명 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/17686
2018년도 KAKAO BLIND RECRUITMENT
"""

"""
(1) 각 file을 돌면서 HEAD, NUMBER, TAIL을 구한다.
(2) HEAD -> NUMBER -> TAIL 순으로 정렬
"""

def getInfo(file):
    idx, curr = 0, 0
    head, number, tail = '', '', ''
    
    while idx < len(file):
        if file[idx].isdigit() == True and head == '':   # HEAD 추출
            head = file[:idx]
            curr = idx
        elif (file[idx].isalpha() == True or file[idx] in '.- ') and head != '':   # NUMBER 추출
            number = file[curr:idx]
            curr = idx
            break   # NUMBER까지 추출하면 나머지 뒤에는 자동적으로 TAIL
        idx += 1
    
    if number == '':
        number = file[curr:]
    else:
        tail = file[curr:]
    
    return [head, number, tail]

def solution(files):
    file_temp = [getInfo(file) for file in files]
    result = sorted(file_temp, key=lambda x: (x[0].upper(), int(x[1])))   # HEAD -> NUMBER
    return [''.join(r) for r in result]
        
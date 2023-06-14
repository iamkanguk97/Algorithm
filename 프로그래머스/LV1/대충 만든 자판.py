"""
프로그래머스 LV1: 대충 만든 자판
https://school.programmers.co.kr/learn/courses/30/lessons/160586
"""

"""
ex) ABCD
1번 키 1번 -> A
2번 키 1번 -> B
2번 키 2번 -> C
2번 키든 1번키든 5번 -> D
"""

def findBestKey(keymap, word):
    result = []
    for km in keymap:
        wc = km.count(word)
        if wc >= 1:
            result.append(km.index(word))
        else:
            result.append(10000)
    
    if min(result) == 10000:
        return -1
    else:
        return min(result)
    
    
def solution(keymap, targets):
    result = []
    
    for target in targets:
        count = 0
        for word in target:
            findResult = findBestKey(keymap, word)   # A가 keymap들 중에서 가장 가까운 곳에 있는걸 찾는다
            if findResult == -1:   # keymap에 글자가 없으면 탐색할 필요가 없이 -1 반환
                result.append(-1)
                break
            else:
                count += (findResult) + 1
        else:
            result.append(count)
    
    return result
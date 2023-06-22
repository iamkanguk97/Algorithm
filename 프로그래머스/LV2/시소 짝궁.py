"""
프로그래머스 LV2: 시소 짝궁 (실패)
https://school.programmers.co.kr/learn/courses/30/lessons/152996
"""

"""
같은 경우
2, 3
2, 4
3, 2
3, 4
4, 2
4, 3
"""

from collections import Counter

def solution(weights):
    weights_dict = Counter(weights)
    answer = 0
    
    wkeys = list(weights_dict.keys())
    for i in range(len(wkeys)):
        for j in range(i, len(wkeys)):
            w1, w2 = wkeys[i], wkeys[j]
            if w1 == w2 and weights_dict[w1] > 1:   # 같은 무게가 여러개
                answer += weights_dict[w1] * (weights_dict[w1] - 1) // 2   # nC2 (예를 들어 100kg 4개면 총 6개 가능)
                continue
                        
            if w1 * 2 == w2 * 3:
                answer += weights_dict[w1] * weights_dict[w2]
            if w1 * 2 == w2 * 4:
                answer += weights_dict[w1] * weights_dict[w2]
            if w1 * 3 == w2 * 2:
                answer += weights_dict[w1] * weights_dict[w2]
            if w1 * 3 == w2 * 4:
                answer += weights_dict[w1] * weights_dict[w2]
            if w1 * 4 == w2 * 2:
                answer += weights_dict[w1] * weights_dict[w2]
            if w1 * 4 == w2 * 3:
                answer += weights_dict[w1] * weights_dict[w2]
                
    return answer
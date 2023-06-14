"""
프로그래머스 LV1: 둘만의 암호
https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""

def solution(s, skip, index):
    result = ''
    skip = list(map(ord, skip))
    
    for i in range(len(s)):
        count = 0
        temp_i = ord(s[i])
        while count < index:
            temp_word = temp_i + 1
            if temp_word > ord('z'):
                temp_word = ord('a')
            if temp_word in skip:
                temp_i = temp_word
                continue
            count += 1
            temp_i = temp_word
        result += chr(temp_i)
    
    return result

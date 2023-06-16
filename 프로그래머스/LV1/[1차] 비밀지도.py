"""
프로그래머스 LV1: [1차] 비밀지도
https://school.programmers.co.kr/learn/courses/30/lessons/17681
2018년도 KAKAO BLIND RECRUITMENT
"""

def makeMap(n, arr):
    result = []
    for a in arr:
        bin_a = str(bin(a))[2:]
        bin_arr = [0] * n
        bin_arr[n-len(bin_a):n] = list(map(int, bin_a))
        result.append(bin_arr)
    return result
            

def solution(n, arr1, arr2):
    map1, map2 = makeMap(n, arr1), makeMap(n, arr2)
    result = []
    for i in range(n):
        temp = "".join(['#' if map1[i][j] + map2[i][j] >= 1 else ' ' for j in range(n)])
        result.append(temp)
    return result
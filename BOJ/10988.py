"""
백준 10988: 팰린드롬인지 확인하기
https://www.acmicpc.net/problem/10988
"""

str = input()   # 문자열 입력받음
reverse_str = str[::-1]   # 입력받은 문자열 거꾸로
result = 0

# 입력받은 문자열이랑 뒤집은 문자열이 같으면 1로 변경
if str == reverse_str:
    result = 1

print(result)
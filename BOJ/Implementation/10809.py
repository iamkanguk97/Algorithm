"""
백준 10809 (B2): 알파벳 찾기
https://www.acmicpc.net/problem/10809

alphabet: abcdefghijklmnopqrstuvwxyz
"""

string = input()
result = [-1] * 26

for idx, s in enumerate(string):
  alphaIdx = ord(s) - ord('a')
  if result[alphaIdx] != -1:
    continue
  else:
    result[alphaIdx] = idx

print(" ".join(map(str, result)))
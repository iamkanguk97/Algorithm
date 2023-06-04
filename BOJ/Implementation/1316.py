"""
백준 1316 (S5): 그룹 단어 체커
https://www.acmicpc.net/problem/1316
"""

word = input()
data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for d in data:
  word = word.replace(d, '@')
print(len(word))
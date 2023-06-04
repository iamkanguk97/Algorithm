"""
백준 1157 (B1): 단어 공부
https://www.acmicpc.net/problem/1157
"""

word = input().upper()
word_set = list(set(word))
result = [0] * len(word_set)

for w in word:
  wIdx = word_set.index(w)
  result[wIdx] += 1

max_value = max(result)

if result.count(max_value) > 1:
  print('?')
else:
  print(word_set[result.index(max_value)])
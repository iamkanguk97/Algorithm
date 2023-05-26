"""
백준 5800 (S5): 성적 통계
https://www.acmicpc.net/problem/5800
"""

k = int(input())   # 반의 수

def getDiff(n, arr):
  diff = []
  for i in range(n-1):
    temp = arr[i] - arr[i+1]
    diff.append(temp)
  return max(diff)

for i in range(k):
  n, *grade = list(map(int, input().split()))
  max_grade = max(grade)
  min_grade = min(grade)
  largest_gap = getDiff(n, sorted(grade, reverse=True))

  print('Class {}'.format(i+1))
  print('Max {}, Min {}, Largest gap {}'.format(max_grade, min_grade, largest_gap))
"""
백준 1475 (S5): 방 번호
https://www.acmicpc.net/problem/1475
"""

N = input()   # 방번호
used = [0] * 10

for n in N:
  target = int(n)   # 방 번호 낱개숫자

  if target == 6 or target == 9:   # 6이나 9이면 숫자 적은곳에 넣어버림
      if used[6] <= used[9]:
        used[6] += 1
      else:
        used[9] += 1
  else:   # 6도 9도 아니면 1 추가
    used[target] += 1


print(max(used))
"""
백준 1195 (G5): 킥다운
https://www.acmicpc.net/problem/1195

도저히 못풀겠다. 구글링을 봐도 다른사람의 풀이가 이해가 1도 안된다.
하루종일 이문제만 봤는데.. 못풀겠다.
"""

def gear(gear1, gear2):
  result = 10000

  for i in range(len(gear1)):
    if gear1[i] != 2 and gear2[0] != 2:   # gear2를 gear1에 맞출 수 있을 때
      made = True
      for j in range(1, len(gear2)):
        idx = i + j
        if idx >= len(gear1):
          break
        else:
          if gear1[idx] == gear2[j]:   # gear1의 블록과 gear2의 블록이 같음
            if gear2[j] == 2:   # 둘다 2면 안됨
              made = False
              break
      if made == True:
        temp = len(gear1[i:])
        if temp >= len(gear2):
          result = len(gear1)
        else:
          result = i + len(gear2)
        break
  return result


gear1 = list(map(int, input()))
gear2 = list(map(int, input()))
result1, result2 = gear(gear1, gear2), gear(gear2, gear1)
print(result1, result2)
print(min(result1, result2))
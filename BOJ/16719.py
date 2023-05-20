"""
백준 16719 (G5): ZOAC
https://www.acmicpc.net/problem/16719
"""

"""
아직 보여주지 않은 문자 중 추가했을때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는것?
ex) STARTLINK을 보여주고 싶다
- A
- AI
- AIK
- ALIK VS AINK => AINK
- ALINK
- ARLINK
- ARTLINK
- SARTLINK
- STARTLINK
"""


def check(arr, idx):
  if len(arr) == 0:
    return

  minLetter = min(arr)  # 사전의 가장 앞쪽 단어
  minLetterIdx = arr.index(minLetter)  # 가장 앞쪽 단어 idx
  result[minLetterIdx + idx] = minLetter
  print("".join(result))  # 결과확인 변수 출력

  # 오른쪽
  check(arr[(minLetterIdx + 1):], idx + minLetterIdx + 1)
  # 왼쪽
  check(arr[:minLetterIdx], idx)


word = input()  # 문자열 입력
result = [''] * len(word)  # 결과확인 변수
check(word, 0)

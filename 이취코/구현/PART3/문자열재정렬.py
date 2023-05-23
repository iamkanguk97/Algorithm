"""
이취코 구현 PART3: 문자열 재정렬
난이도: 1
기출: Facebook 인터뷰
"""

S = input()  # 문자열
alpha = []  # 알파벳 저장 배열
number = 0  # 숫자 합 저장 변수

for w in S:
  if w.isalpha() == True:  # 알파벳이면
    alpha.append(w)
  else:  # 숫자면
    number += int(w)

alpha.sort()  # 오름차순 정렬

if number != 0:  # 숫자가 0이 아니면
  alpha.append(str(number))

print("".join(alpha))


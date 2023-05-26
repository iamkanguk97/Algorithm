"""
백준 2161 (S5): 카드1
https://www.acmicpc.net/problem/2161
"""

from collections import deque

n = int(input())   # 카드 개수
card = deque([i+1 for i in range(n)])   # 카드 queue 설정
removedCard = []   # 버린 카드들 리스트

while len(card) > 1:
  removedCard.append(card.popleft())   # 제일 위에있는 카드 버림
  topCard = card.popleft()   # 버린 후 맨 위에있는 카드 뺌
  card.append(topCard)   # 빼서 맨 아래 넣음
  
removedCard.append(card[0])   # 제일 마지막에 남은 카드번호 삽입

for i in range(len(removedCard)):
  print(removedCard[i], end = ' ')
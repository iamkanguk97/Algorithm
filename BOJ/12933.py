"""
백준 12933 (S3): 오리
https://www.acmicpc.net/problem/12933

많이 어려웠다...
"""

duck = input()
visited = [False] * len(duck)  # 각 문자를 방문했는지 확인하는 변수
count = 0  # 오리 수
quack = 'quack'  # 오리의 울음소리 저장


def quackCheck(idx):
  global count  # count 전역변수 설정
  qIdx = 0  # quack 변수를 순회할 index
  check = True  # quack을 처음 완성한건지 아닌지

  for i in range(idx, len(duck)):
    if quack[qIdx] == duck[i] and visited[i] == False:
      visited[i] = True  # 방문처리
      if duck[i] == 'k':  # k를 만났다는건 quack 1개가 완성되었다는 뜻
        if check == True:  # 처음 quack을 완성한 경우
          count += 1  # 오리 수 추가
          check = False
        qIdx = 0  # quack 순회 index 초기화
        continue  # 반복문 다시 진행
      qIdx += 1  # k가 아니면 quack index 변경


# 여기가 제일 중요한듯... 오리울음 문자열이 5의 배수가 아니면 로직 자체가 수행이 안됨
if len(duck) % 5 != 0:
  print(-1)
  exit()
else:
  for i in range(len(duck)):
    if duck[i] == 'q' and visited[i] == False:  # 해당 문자가 q이고 방문한적이 없음
      quackCheck(i)  # 찾기 시작

if not all(visited) or count == 0:
  print(-1)
else:
  print(count)

"""
백준 15787 (S2): 기차가 어둠을 헤치고 은하수를
https://www.acmicpc.net/problem/15787
"""

n, m = map(int, input().split())  # n: 기차 수, m: 명령 수
trains = [[0] * 20 for _ in range(n)]  # 각 기차마다 20개 좌석 할당

for i in range(m):
  command = list(map(int, input().split()))  # 명령 입력받음

  if command[0] == 1:  # 1번 명령
    trainNumber = command[1] - 1  # 기차 번호
    seatNumber = command[2] - 1  # 좌석 번호

    if trains[trainNumber][seatNumber] == 0:  # 좌석이 비어있으면 입석 처리
      trains[trainNumber][seatNumber] = 1
  elif command[0] == 2:  # 2번 명령
    trainNumber = command[1] - 1  # 기차 번호
    seatNumber = command[2] - 1  # 좌석 번호

    if trains[trainNumber][seatNumber] == 1:  # 좌석에 타있으면 하차 처리
      trains[trainNumber][seatNumber] = 0
  elif command[0] == 3:  # 3번 명령
    trainNumber = command[1] - 1
    selectedTrain = trains[trainNumber]
    temp = selectedTrain[0]
    _temp = -1
    for i in range(1, len(selectedTrain)):
      _temp = selectedTrain[i]  # 현재값 미리저장
      selectedTrain[i] = temp  # 이전 값 가져옴
      temp = _temp

    selectedTrain[0] = 0  # 맨 앞자리는 공석처리
    trains[trainNumber] = selectedTrain
  elif command[0] == 4:  # 4번 명령
    trainNumber = command[1] - 1
    selectedTrain = trains[trainNumber]
    temp = selectedTrain[len(selectedTrain) - 1]
    _temp = -1
    for i in range(len(selectedTrain)-2, -1, -1):
      _temp = selectedTrain[i]
      selectedTrain[i] = temp
      temp = _temp

    selectedTrain[len(selectedTrain)-1] = 0   # 맨 뒷자리 공석처리
    trains[trainNumber] = selectedTrain


records = []
count = 0

for train in trains:
  checkResult = False
  if len(records) != 0:
    for record in records:
      if train == record:
        checkResult = True
        break

    if checkResult == False:
      count += 1
  else:
    count += 1
    
  records.append(train)


print(count)
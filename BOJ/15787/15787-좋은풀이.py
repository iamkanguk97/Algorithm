n, m = map(int, input().split())  # n: 기차 수, m: 명령 수
trains = [[0] * 20 for _ in range(n)]  # 각 기차마다 20개 좌석 할당

for i in range(m):
  command = list(map(int, input().split()))  # 명령 입력받음

  if command[0] == 1:  # 1번 명령
    trains[command[1]-1][command[2]-1] = 1   # 굳이 좌석이 비어있는지 확인할 필요 없음
  elif command[0] == 2:  # 2번 명령
    trains[command[1]-1][command[2]-1] = 0  # 마찬가지로 좌석이 비어있지 않은지 확인할 필요 없음
  elif command[0] == 3:  # 3번 명령
    """
    여기가 제일 어이가 없었음..
    나는 임시값을 2개나 받았는데 생각해보니 거꾸로 하면 전혀 추가값이 필요없다는걸...
    왜 이걸 생각하지 못했을까
    """
    for j in range(19, 0, -1):
      trains[command[1]-1][j] = trains[command[1]-1][j-1]
    trains[command[1]-1][0] = 0
  elif command[0] == 4:  # 4번 명령
    for j in range(19):
      trains[command[1]-1][j] = trains[command[1]-1][j+1]
    trains[command[1]-1][19] = 0


records = []
count = 0

for i in range(n):
  if trains[i] not in records:
    records.append(trains[i])
    count += 1


print(count)
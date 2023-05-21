"""
백준 20207 (G5): 달력
https://www.acmicpc.net/problem/20207

하다가 포기함..
"""

n = int(input())  # 일정의 개수
schedule = [tuple(map(int, input().split())) for _ in range(n)]  # 일정 리스트
schedule.sort(key=lambda x:
              (x[0], -abs(x[0] - x[1])))  # 시작일 기준 정렬, 시작일이 같으면 일정기간이 긴 것 먼저

calender_min = min(schedule, key=lambda x: x[0])[0]  # 달력 시작점
calender_max = max(schedule, key=lambda x: x[1])[1]  # 달력 종료점
calender = [[0] * (calender_max + 1)]  # 달력 배열 생성


# 일정 생성 함수
def makeSchedule(row, schedule_start, schedule_end):
  for s in range(schedule_start, schedule_end + 1):
    calender[row][s] = 1


# 다차원 배열 자르는 함수
def cutArray(start, end):
  temp = calender
  for i in range(len(temp)):
    temp_data = temp[i][start:end]
    temp[i] = temp_data

  return temp


# 면적 구하는 로우
def getActiveRow(arr):
  rcount = 0
  for crow in arr:
    if crow.count(1) == 0:
      break
    rcount += 1

  return rcount


# 첫 일정 처리
makeSchedule(0, schedule[0][0], schedule[0][1])

# 두번째 일정부터 시작
for i in range(1, n):
  schedule_start = schedule[i][0]  # 일정 시작
  schedule_end = schedule[i][1]  # 일정 종료

  # 일정이 모두 차있으면 row하나더 생성해서 넣어주면 됨
  if all(crow[schedule_start] == 1 for crow in calender):
    calender.append([0] * (calender_max + 1))  # 새로운 행 생성
    makeSchedule(len(calender) - 1, schedule_start, schedule_end)
  else:  # 일정이 모두 차있지 않음
    for crow in range(len(calender)):
      if calender[crow][schedule_start] == 0:  # 해당 달력로우에 일정이 안잡혀있으면
        makeSchedule(crow, schedule_start, schedule_end)  # 일정생성
        break

for asdf in calender:
  print(asdf)

# 코팅지 로직 진행
# 로우들 중 하나라도 1이 포함되어 있는 부분까지 확인
isFull = True
start = calender_min
result = 0
for date in range(calender_min, calender_max + 1):
  if all(crow[date] == 0 for crow in calender) == True:
    print(start, date)
    cutCalender = cutArray(start, 12)  # 달력 자르기
    print(cutCalender)
    # activeRows = getActiveRow(cutCalender)
    # result += activeRows * (date - start)
    # start = date + 1
  
#   if all(crow[date] == 0 for crow in calender):  # 해당 일에 일정이 모두 비어있으면
#     cutCalender = cutArray(calender_min, date)  # 달력 자르기
#     activeRows = getActiveRow(cutCalender)
#     result += activeRows * (date - start)
#     start = date + 1

# print(result)
# print(temp)

# result = temp * (calender_max - calender_min + 1)
# print(result)

# print(calender[0].count(1))

# if any(calender[crow].count(1) != 0 for crow in calender):
#   print('hello')

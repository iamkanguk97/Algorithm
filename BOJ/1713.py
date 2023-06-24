"""
백준 1713번: 후보 추천하기 (S1)
https://www.acmicpc.net/problem/1713
"""

n = int(input())   # 사진틀 개수
recommend_count = int(input())   # 전체 학생의 총 추천 횟수
recommended_students = list(map(int, input().split()))   # 추천받은 학생 번호들

# photo_box = {1: (1, 2), 2: (2, 3)}
# print(photo_box.items())
photo_box = {}   # 사진틀 상태 저장 (학생번호: (추천받은 횟수, 기간))
for rs in recommended_students:
    if rs in photo_box.keys():   # 사진틀에 해당 학생 번호가 있는 경우 추천수만 증가
       photo_box[rs][0] += 1
    else:   # 사진틀에 학생 번호가 없음
      if len(photo_box) == n:   # 사진틀이 꽉 차있는 경우
          sorted_photo = sorted(photo_box.items(), key=lambda x: (x[1][0], -x[1][1]))   # 추천받은 횟수, 오래된 기간 순으로 정렬
          photo_box.pop(sorted_photo[0][0])   # 정렬한 사진틀에서 맨 앞에 원소 삭제
      photo_box[rs] = [1, 0]
    
    # 모든 사진틀에 기간 1 추가
    for photo in photo_box:
      photo_box[photo][1] += 1


print(" ".join(map(str, sorted(photo_box.keys()))))
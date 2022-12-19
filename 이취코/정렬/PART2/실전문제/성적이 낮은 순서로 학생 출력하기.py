# 정렬 PART2 실전문제) 성적이 낮은 순서로 학생 출력하기

n = int(input())   # N 입력받기
data = []

# N만큼 학생 정보 받아오기 + data 리스트에 저장
for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

# 정렬 기준을 정해주는 function 선언
def setting(data):
    return data[1]

# 정렬 라이브러리 사용
result = sorted(data, key=setting)
# result = sorted(data, key=lambda student: student[1])   # 여기서 setting이라는 함수 선언도 좋지만 Lambda 표현식을 사용하면 더 좋다

for i in result:
    print(i[0], end=' ')
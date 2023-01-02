# 정렬 PART3 - 강욱 Version) 실패율
# 2019년도 카카오 신입 공채 1차 코딩테스트
# https://programmers.co.kr/learn/courses/30/lessons/42889

# 해결 시 주의 사항!
# - "스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다"
# - 이부분에 대한 조건이 꼭 필요함!

# Review
# - 반복문을 줄여서 코드 개선을 할 수 있었을 거 같은데 하지 못한점이 아쉬움.


def solution(N, stages):
    users = len(stages)   # 총 사용자
    user_stage_count = [0] * N   # 각 stage에 남아있는 사용자들 수 리스트
    result = []   # 결과 저장 리스트

    stages.sort()   # 오름차순으로 stage 정렬

    # stage에 남아있는 사용자들 수를 user_stage_count에 저장
    for i in range(users):
        if stages[i] > N:
            continue
        else:
            user_stage_count[stages[i] - 1] += 1

    for i in range(len(user_stage_count)):
        print(
            '{}번 스테이지에는 총 ${}명의 사용자가 도전했으며, 이 중 {}명의 사용자가 아직 클리어하지 못했습니다. 따라서 {}번 스테이지의 실패율은 다음과 같습니다.'
        .format(i+1, users, user_stage_count[i], i+1))
        
        if users > 0:
            fail_rate = user_stage_count[i] / users   # 실패율 계산
        else:
            fail_rate = 0
        result.append((i+1, fail_rate))   # result 배열에 스테이지 번호와 실패율 append
        print('-- {}번 스테이지 실패율: {}/{} ({})'.format(i+1, user_stage_count[i], users, fail_rate))

        users -= user_stage_count[i]   # 계산 이후에는 전체 유저에서 해당 사용자 카운트만큼 빼준다.
    
    # 실패율을 기준으로 내림차순으로 정렬. 스테이지 번호가 같을 때는 낮은 번호 순으로 정렬
    result.sort(
        reverse = True,
        key = lambda x: (x[1], -x[0])
    )
    result = [ x[0] for x in result ]

    return result    
        
    

n = int(input())   # 총 스테이지 개수
stages = list(map(int, input().split()))   # 각 원소는 사용자가 현재 도전중인 스테이지 번호
result = solution(n, stages)
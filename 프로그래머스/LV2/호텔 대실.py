"""
프로그래머스 LV2: 호텔 대실
https://school.programmers.co.kr/learn/courses/30/lessons/155651
"""

"""
[14:10/19:20, 14:20/15:20, 15:00/17:00, 16:40/18:20, 18:20/21:20]

- 2시10분~19시20분: 방1개
- 2시20분~15시20분: 방2개
- 3시~5시: 방3개
- 4시40분~6시20분: 2번방 사용가능
- 6시20분~9시20분: 3번방 사용가능
따라서 최소 3개의 방이 필요하다.
"""

def addTime(time):
    h, m = time.split(':')
    m = int(m) + 10
    
    if m >= 60:
        h = str(int(h) + 1).zfill(2)
        m -= 60
    
    return h + ':' + str(m).zfill(2)


def solution(book_time):
    room = []
    book_time = sorted(book_time, key=lambda x: x[0])   # 입실시간 기준으로 정렬
    
    for book in book_time:
        enter_t, exit_t = book[0], book[1]
        if len(room) != 0:   # 첫 입장일 때
            # 기존에 있던 방들 확인해서 입장할 수 있는 방이 있으면 거기로 입장!
            for idx, r in enumerate(room):   # 방의 정보들
                r_enter, r_exit = r[0], r[1]
                addedExit = addTime(r_exit)   # 10분 추가
                if addedExit <= enter_t:
                    room.pop(idx)
                    break
        room.append((enter_t, exit_t))
    
    return len(room)
"""
백준 17413번: 단어 뒤집기 2
https://www.acmicpc.net/problem/17413

- 로직을 간단하게 생각해보기
- word += w가 아니라 word = w + word가 제일 중요함!!!!!
"""

S = list(input())

tag_check = False   # 괄호 확인
word = ''   # 단어 임시 저장소
result = ''   # 결과값

for w in S:
    print(w)
    if tag_check == False:   # 괄호를 만난적이 없는 부분
        if w == '<':   # 괄호를 만났다면
            tag_check = True   # 괄호 확인 True로 변경
            word += w
        elif w == ' ':   # 공백을 만났다면
            word += w
            result += word   # 결과값 저장
            word = ''   # 단어 임시 저장소 초기화
        else:   # 일반 문자
            word = w + word   # 핵심 포인트! 거꾸로 더해주기
    elif tag_check == True:  # 괄호를 만난 뒤
        word += w
        if w == '>':   # 닫히는 괄호를 만난 경우
            tag_check = False   # 괄호 확인 False로 변경
            result += word   # 결과값 저장
            word = ''   # 단어 임시 저장소 초기화
            
print(result + word)
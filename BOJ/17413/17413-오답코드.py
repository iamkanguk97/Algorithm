"""
백준 17413번: 단어 뒤집기 2
https://www.acmicpc.net/problem/17413

오답이유)
- 너무 어렵게 접근을 하려고 했던거 같음.. 너무 연습이 많이 필요할듯. 
- 진짜 무작정 하려고 하니까 너무 산으로 갔던거 같다.
- 리스트로 할 수 있다는 포인트를 못잡은 것 같음!
"""

S = input()

front = 0
back = 0
result_arr = []

print(len(S))

while back <= len(S) - 1:
    print(front, back)
    # 공백 또는 < 만날때까지 반복문 순회
    while S[back] != ' ' and S[back] != '<' and back < len(S) - 1:
        back += 1

    # 멈춘 부분이 <이면 >만날때까지 순회
    if S[back] == '<':
        while S[back] != '>':
            back += 1
        result_arr.append(S[front+1:back+1])
        front = back
        back += 1
    else:   # 멈춘 부분이 공백이면 front까지의 문자열 Reverse
        if S[front] == '>':
            front = back
            back += 1
            continue
        result_arr.append(S[front+1:back][::-1])   # 뒤집은 문자 배열에 삽입
        result_arr.append(S[back])   # 공백 부분일거임 -> 공백도 배열에 삽입
        front = back   # front를 back으로 당김
        back += 1   # back 1칸 이동

print(result_arr)
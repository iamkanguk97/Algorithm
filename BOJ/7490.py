"""
벡준 7490 (G4): 0 만들기
https://www.acmicpc.net/problem/7490
"""
"""
1+2 3 4 5 6 7 -> 1+2+3 -> 1+2+3+4 -> 1+2+3+4+5 -> ...
                                               -> ...
                                               -> ...
                                  -> 1+2+3+4 5 -> 1+2+3+4 5+6
                                               -> 1+2+3+4 5 6
                                               -> 1+2+3+4 5-6
                                  -> 1+2+3+4-5
                       -> 1+2+3 4
                       -> 1+2+3-4
              -> 1+2 3
              -> 1+2-3
"""

def recursion(now, answer, tc):
    if now == tc + 1:
      _answer = answer.replace(' ', '')
      if eval(_answer) == 0:
         print(answer)
      return
    
    recursion(now+1, answer+' '+str(now), tc)
    recursion(now+1, answer+'+'+str(now), tc)
    recursion(now+1, answer+'-'+str(now), tc)


tc_count = int(input())   # 테스트 케이스 개수
for _ in range(tc_count):
    tc = int(input())   # 테스트 케이스 자연수
    recursion(2, '1', tc)
    print()
# 백준 20546번: 기적의 매매법
# https://www.acmicpc.net/problem/20546

credit = int(input())   # 준현이와 성민이에게 주어진 현금
stock = list(map(int, input().split())) # 1일부터 14일까지의 주가

def method_j(stock):
    j_credit = credit
    j_totalBuyCount = 0

    for s in stock:
        if j_credit == 0:   # 현금이 0원이면 반복문 탈출
            break
        if j_credit >= s:
            j_totalBuyCount += (j_credit // s)   # 준현이가 산 최대 주식 개수 더해줌
            j_credit = j_credit % s   # 나머지 거스름돈으로 세팅
    
    return j_totalBuyCount, j_credit


def method_s(stock):
    s_credit = credit
    s_totalBuyCount = 0

    for s in range(3, len(stock)):
        bigCheck = 0
        smallCheck = 0
        for j in range(s-1, s-3, -1):
            if stock[j] > stock[j-1]:   # 3일연속 가격이 하락하는지 확인
                bigCheck += 1
                smallCheck += 0
            elif stock[j] < stock[j-1]:
                smallCheck += 1
                bigCheck += 0
            else:
                break
        
        if smallCheck == 2:   # 전량 매수
            if s_credit == 0:
                continue
            s_totalBuyCount += (s_credit // stock[s])
            s_credit = s_credit % stock[s]
        elif bigCheck == 2:   # 전량 매도
            if s_totalBuyCount == 0:
                continue
            s_credit += (s_totalBuyCount * stock[s])
            s_totalBuyCount = 0
        else:
            continue
            
    return s_totalBuyCount, s_credit
            

j_totalBuyCount, j_credit = method_j(stock)
s_totalBuyCount, s_credit = method_s(stock)

j_asset = j_credit + (stock[-1] * j_totalBuyCount)
s_asset = s_credit + (stock[-1] * s_totalBuyCount)

if j_asset > s_asset:
    print('BNP')
elif j_asset < s_asset:
    print('TIMING')
else:
    print('SAMESAME')
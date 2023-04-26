# 백준 20546번: 기적의 매매법
# https://www.acmicpc.net/problem/20546

credit = int(input())   # 준현이와 성민이에게 주어진 현금
stock = list(map(int, input().split())) # 1일부터 14일까지의 주가

# 준현이 계산 방법 함수
def method_j(stock):
    j_credit = credit   # 준현이 현금
    j_totalBuyCount = 0   # 준현이가 산 주식 개수

    for s in stock:
        if j_credit == 0:   # 현금이 0원이면 반복문 탈출 -> 매도를 못하니까
            break
        if j_credit >= s:
            j_totalBuyCount += (j_credit // s)   # 준현이가 산 최대 주식 개수 더해줌
            j_credit = j_credit % s   # 나머지 거스름돈으로 세팅
    
    return j_totalBuyCount, j_credit


# 성민이 계산 방법 함수
def method_s(stock):
    s_credit = credit   # 성민이 현금
    s_totalBuyCount = 0   # 성민이가 산 주식 개수

    for s in range(3, len(stock)):
        # bigCheck랑 smallCheck는 전일 대비 3일간 상승세인지 하향세인지 확인하기 위한 변수 세팅
        bigCheck = 0
        smallCheck = 0
        for j in range(s-1, s-3, -1):
            if stock[j] > stock[j-1]:   # 3일연속 가격이 상승하는지 확인 (매도)
                bigCheck += 1
                smallCheck += 0
            elif stock[j] < stock[j-1]:   # 3일연속 가격이 하락하는지 확인 (매수)
                smallCheck += 1
                bigCheck += 0
            else:
                break
        
        if smallCheck == 2:   # 전량 매수
            if s_credit == 0:   # 현금이 없으면 매수를 못함
                continue
            s_totalBuyCount += (s_credit // stock[s])   # 매수한 주식만큼 더해줌
            s_credit = s_credit % stock[s]   # 잔돈 세팅
        elif bigCheck == 2:   # 전량 매도
            if s_totalBuyCount == 0:   # 주식을 산게 없으면 매도를 못함
                continue
            s_credit += (s_totalBuyCount * stock[s])   # 당일 주식값에 산 주식만큼 곱해서 세팅
            s_totalBuyCount = 0   # 매도했기 때문에 가지고있는 주식은 없음
        else:
            continue
            
    return s_totalBuyCount, s_credit
            

j_totalBuyCount, j_credit = method_j(stock)
s_totalBuyCount, s_credit = method_s(stock)

# 1월 14일의 자산 = (현금 + 1월 14일의 주가 × 주식 수)
j_asset = j_credit + (stock[-1] * j_totalBuyCount)
s_asset = s_credit + (stock[-1] * s_totalBuyCount)

# 준현이 > 성민이
if j_asset > s_asset:
    print('BNP')
# 성민이 > 준현이
elif j_asset < s_asset:
    print('TIMING')
# 준현이 = 성민이
else:
    print('SAMESAME')
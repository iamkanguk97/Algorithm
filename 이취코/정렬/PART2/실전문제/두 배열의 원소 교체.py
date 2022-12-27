# 정렬 PART2 실전문제) 두 배열의 원소 교체

n, k = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

alist.sort()   # alist는 오름차순으로 정렬
blist.sort(reverse=True)   # blist는 내림차순으로 정렬

# K만큼 바꿔치기 연산 수행
for i in range(k):
    if alist[i] < blist[i]:   # A의 원소가 B의 원소보다 작을 경우 SWAP
        alist[i], blist[i] = blist[i], alist[i]
    else:   # A의 원소가 B의 원소보다 클 경우 반복문 탈출 -> 뒤에는 보나마나임
        break        

print(sum(alist))
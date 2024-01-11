from itertools import product

a, b = map(str, input().split(' '))
la, lb = len(a), len(b)

result = 0
for i in range(la, lb+1):
  combList = list(product([4, 7], repeat = i))
  for comb in combList:
    number = int(''.join(map(str, comb)))
    if int(a) <= number <= int(b):
      result += 1

print(result)
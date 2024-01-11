def dfs(lower, upper, depth, num):
  result = 0

  if depth >= 10 or num > upper:
    return 0
  if lower <= num <= upper:
    result += 1

  result += dfs(lower, upper, depth+1, num*10+4)
  result += dfs(lower, upper, depth+1, num*10+7)

  return result

a, b = map(int, input().split(' '))
result = dfs(a, b, 0, 0)
print(result)
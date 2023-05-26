"""
백준 1969 (S4): DNA
https://www.acmicpc.net/problem/1969
"""

n, m = map(int, input().split())  # n: DNA수, m: DNA 문자열 길이
dna = [input() for _ in range(n)]   # dna 리스트

# dna 문자 개수 확인 함수
def dna_counting(a, b):
  global dna_count
  
  if dna[a][b] == 'A':
    dna_count[0] += 1
  elif dna[a][b] == 'C':
    dna_count[1] += 1
  elif dna[a][b] == 'G':
    dna_count[2] += 1
  elif dna[a][b] == 'T':
    dna_count[3] += 1

# 숫자 -> dna 변환
def get_dna(idx):
  if idx == 0:
    return 'A'
  elif idx == 1:
    return 'C'
  elif idx == 2:
    return 'G'
  else:
    return 'T'


new_dna = ''   # dna 문자열
hd = 0   # hamming distance의 총합
for i in range(m):
  dna_count = [0, 0, 0, 0]   # A-C-G-T
  for j in range(n):
    dna_counting(j, i)
  max_dna_count_idx = dna_count.index(max(dna_count))   # 많이 나온 dna 문자 index
  dna_letter = get_dna(max_dna_count_idx)   # 많이 나온 dna 문자
  new_dna += dna_letter
  hd += (n - max(dna_count))   # 많이 나온 문자수를 뺀 나머지


print(new_dna)
print(hd)
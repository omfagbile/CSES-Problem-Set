dna = input()
n = len(dna)

ans = 0 

for i in range(n):
  j = 0 #end pointer
  while dna[i] == dna[j]:
    j += 1
  ans = max(ans, j-i)


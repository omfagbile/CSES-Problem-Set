dna = input()
n = len(dna)

ans = 0 

for i in range(n):
  j = i #end pointer
  while j+1<=n-1 and dna[i] == dna[j+1]:
    j += 1
  ans = max(ans, j-i+1)

print(ans)

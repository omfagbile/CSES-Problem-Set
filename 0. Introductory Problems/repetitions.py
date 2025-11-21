s = input()
n = len(s)

ans = 0 
lis = 1

for i in range(1,n):
  if s[i] == s[i-1]:
    lis += 1
  else: 
    lis = 1
  ans = max(ans, lis)

print(ans)

n = int(input())
arr = [int(ch) for ch in input().split()]
ans = 0 #number of moves needed at first position
for i in range(1, n):
    if arr[i-1] > arr[i]:
        ans += arr[i-1]-arr[i]
        arr[i]=arr[i-1]
print(ans)        
    

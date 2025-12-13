n = int(input())
if n == 3 or n == 2:
    print("NO SOLUTION")
else: 
    arr = []
    if n%2 == 1:
        arr.append(n)
        n = n-1
    for i in range(1,n+1):
        if i <= n/2:
            arr.append(-2*i+n+1)
        else:
            arr.append(-2*i+2*n+2)
    print(*arr)
             
def solve(y, x):
    m, n, i = y, x, 0 #max, min, index of min
    if x>y: 
        m, n, i = x, y, 1

    if (m+i)%2 == 0: 
        print(m**2 - n + 1)
    else:
        print((m-1)**2 + n)

    #alternatively
    #t  = (m+i) % 2 
    #print( (m-t)**2 + n*(-1)**(t+1) + int(not(t)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        y, x = [int(i) for i in input().split()] 
        solve(y,x)
        

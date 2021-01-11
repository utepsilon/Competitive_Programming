
n = int(input())
for __ in range(n):
    k = int(input())
    ans = 0
    i = 1
    while(k//(5**i)>=1):
        ans += k//(5**i) 
        i+=1 
    print(ans)
        
    
        
        
        
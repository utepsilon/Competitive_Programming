t = int(input())
for __ in range(t):
    g = int(input())
    for __ in range(g):
        i,n,q = map(int,input().split())
        if i==1 and q==1:
            print(n//2)
        elif i==1 and q==2:
            if n%2==0:
                print(n//2)
            else:
                print((n//2)+1)
        elif i==2 and q==1:
            if n%2==0:
                print(n//2)
            else:
                print((n//2)+1)
        else:
            print(n//2)
                
            
            

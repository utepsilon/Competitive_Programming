def Prime(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True 
    for i in range(5,int(n**(1/2))+1):
        if n%i==0 or n%(i+2)==0:
            return False
    return True




t = int(input())
for i in range(t):
    n = int(input())
    print(Prime(n))
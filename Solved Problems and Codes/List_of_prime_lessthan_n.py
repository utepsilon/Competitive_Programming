def num_of_prime(n):
    primes = [True]*(n+1 )
    primes[0],primes[1]=False,False
    for i in range(1,int(n**(1/2))+1):
        if primes[i]:
            for j in range(i**2,n+1,i):
                if j%i==0:
                    primes[j]=False
    
            
    return primes

t = int(input())
for i in range(t):
    n  = int(input())
    li = num_of_prime(n)
    print(li.count(True))



def factors(n):
    s = set();
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
t = int(input())
for i in range(t):
    n = int(input())
    print(*factors(n))


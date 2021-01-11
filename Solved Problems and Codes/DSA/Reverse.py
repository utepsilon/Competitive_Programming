# cook your dish here
n = int(input())
while(n>0):
    n-=1 
    k = input()
    x = [x for x in k]
    l = ''.join(x[::-1])
    print(int(l))
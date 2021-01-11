arr = [1]
def factdp(N):
    global arr
    if N<len(arr):
        return arr[N]
    else:
        arr.append(N*factdp(N-1))
        return arr[N]
        
    
n = int(input())
for __ in range(n):
    k = int(input())
    l = str(factdp(k))
    l = l[::-1]
    ans = 0
    for i in range(len(l)):
        if l[i]=='0':
            ans = i+1
        else:
            break
    print(ans)
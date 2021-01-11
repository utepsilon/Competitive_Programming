import heapq 
t = int(input())
for __ in range(t):
    n,z = map(int,input().split())
    arr = [int(x) for x in input().split()]
    arr= [-1*x for x in arr]
    arr1  = []
    c = 0
    heapq.heapify(arr1)
    for i in arr:
        heapq.heappush(arr1,i)
    while(z>0 and -1*arr1[0]>0):
        x = heapq.heappop(arr1)
        x = x*-1 
        z = z - x 
        x = x//2 
        heapq.heappush(arr1,-1*x)
        c+=1 
    if z<=0:
        print(c)
    else:
        print("Evacuate")
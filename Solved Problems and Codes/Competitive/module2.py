"""Problem :https://www.codechef.com/LRNDSA04/problems/ASHIGIFT"""
t = int(input())
for __ in range(t):

    x = int(input())
    arr = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    q1 = []
    q2 = []
    for i in range(0,len(arr)-1,2):
        q1.append([arr[i+1],arr[i+2]])
    #for i in range(arr[0]):
        #print(q1.get())
    if len(arr1)>1:
        for i in range(0,len(arr1)-1,3):
            q2.append([arr1[i+1],arr1[i+2],arr1[i+3]])
            #print(q2.get()
    print(q1,q2)
    hi = 10**9 
    low = 1  
    while(lo>=hi):
        mid = (hi+low)//2
        x1 = 0
        for i in q1:
            if i[0]<=x:
                x1+= i[1]
        if x1+1==mid:
            print(mid)
            break
        elif x1-1==mid:
            print(mid)
            break
        elif x1==mid:
            print(x1+1)
            break
        elif x1>mid:
            lo = mid+1 
        else:
            hi = mid-1 


         
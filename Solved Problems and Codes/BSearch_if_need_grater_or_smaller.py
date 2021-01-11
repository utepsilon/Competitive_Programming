import bisect 
def Bsearch(arr,k,beg,end):
    mid = (beg+end)//2
    if beg>end:
        return -1
    if arr[beg]>k:
        return beg 
    elif arr[mid]<n and arr[mid+1]>n:
        return mid+1 
    else:
        if arr[mid]>k:
            return Bsearch(arr,n,beg,mid-1)
        if arr[mid]<k:
            return Bsearch(arr,n,mid+1,end)
"""Binary Search 

1> Basic problem 

We've given an array of length n 
we  have to searcg q qyery in an array 
"""

n = int(input())
arr = [int(x) for x in input().split()]

# if we have any monotonic function such that f(i+1)>=f(i) or vice versa 

# if f(i)<x) then we don't have to check  index below i 

# to set the valid range we can check the middle element 

x = int(input())
lo = 0
hi = n

while(lo<=hi):
	if mid = lo+hi//2
	if arr[mid]<x:
		lo = mid+1 
	elif arr[mid]>x:
		hi = mid-1 
	else:
		print("Yes")
		break







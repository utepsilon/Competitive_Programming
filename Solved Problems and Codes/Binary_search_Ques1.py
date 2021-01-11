""" 

given an int k where k<= 10e17

you have to find two int A and B such that A+B=k and A*B= k
"""

k = int(input())
#Bruteforce will give TLE 

# A*B = K and A+B = k so B = K-A then A*(K-A) = k is a function 

# A*(K-A) is a monotonic function till k/2 
lo = 0
hi = k/2

while(lo<=hi):
	mid = (lo+hi)/2
	f = mid*(k-mid)
	if f==k:
		print(mid,k-mid)
	elif f>k:
		hi = mid-1 
	else:
		lo = mid+1 



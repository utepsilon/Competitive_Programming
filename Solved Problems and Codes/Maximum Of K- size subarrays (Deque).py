
n,k = map(int,input().split())
arr = [int(x) for x in input().split()]
for i in range(n-k+1):
	print(max(arr[i:i+k]),end=" ")
"""
Given an array A of size 'N' and an integer k, find the maximum for each and every contiguous subarray of size k.

Input :

First line contains 2 space separated integers 'N' and 'k' .
Second line contains 'N' space separated integers denoting array elements.
Output:

Space separated Maximum of all contiguous sub arrays of size k.
Constraints :

1<= N <=10^5
1<= Ai <=10^9
1<= k <=N
SAMPLE INPUT 
9 3
1 2 3 1 4 5 2 3 6
SAMPLE OUTPUT 
3 3 4 5 5 5 6
"""
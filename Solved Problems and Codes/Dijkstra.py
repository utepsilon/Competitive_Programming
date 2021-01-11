import heapq
import collections 

def shortestpath(graph,s,d):
	h = []
	#keep a track of the vertices 
	#when we pop heap will pop vertix with least weight 
	#greedy approach 

	heapq.heappush(h,(0,s))
	path = []
	while len(h)>0:
		currcost,currver = heapq.heappop(h)
		if currver == d:
			print(s,d,currcost,end= "           "  )
			return
		for neigh,neighcost in graph[currver]:
			heapq.heappush(h,(currcost+neighcost,neigh))
			




graph = collections.defaultdict(list)

v,e = map(int,input().split())
for i in range(e):
	u,v,w = input().split()
	graph[u].append((v,int(w)))
s,d = input().split()
shortestpath(graph,s,d)

""" 
Input 
6 7 
A B 4
A C 2 
B C 5
B D 10
C E 3
D F 11
E D 4
A D
"""

import collections

graph = collections.defaultdict(list)
t = int(input())
while(t>0):
	t-=1
	u,v = map(int,input().split())# u = total nodes , v = Edges 
	for i in range(v):
		a,b = input().split()
		graph[a].append(b)
		graph[b].append(a)
	print(graph)

"""

Input pattern Example 

1
4 4
A B
B C
C D
D A

OP: defaultdict(<class 'list'>, {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'A']})
"""
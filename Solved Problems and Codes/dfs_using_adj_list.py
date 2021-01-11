import collections 

t = int(input())
def dfs(graph,visited,start,path):
    visited[start] = 'True'
    path.append(start)
    for n in graph[start]:
        #n is neighbour 
        if visited[n]==False:
            dfs(graph,visited,n,path)
    return path
    
while(t>0):
	t -=1
	v,e = map(int,input().split())
	graph = collections.defaultdict(list)
	for i in range(e):
	    a,b = input().split()
	    graph[a].append(b)
	    graph[b].append(a)
	#print(graph)
	path = []
	visited = collections.defaultdict(bool)
	start = "A"
	traversedpath = dfs(graph,visited,start,path)
	print(*traversedpath)
	
	"""
	1
7 9 
A B 
A C 
A F 
C E 
C F 
C D
D E 
D G 
G F

Time(sec) : 0.02Memory(MB) : 0.125
Output:
A B C E D G F
"""
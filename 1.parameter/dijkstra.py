'''
Let's define some data :
On the St Exupery Airport in Lyon, France, we are landing on the runway 18 R (South)
We suppose we can stop the plane at the beginning of the runway, so we can take all exit lane.
Finally, we suppose we are going to the principal terminal, near the exit R5 --> F.
We are going to name this airport P4.
'''

import sys
from heapq import *
 
inf = int(1e12)
index = 0
with open("format_dijkstra.txt", "r") as f:
	for line in f:
		if index == 0:
			n, m = map(int, line.split())
			parent = [-1]*n
			dis = [inf]*n
			graph = [[] for i in range(n)]
			dis[0] = 0
			index += 1
		else:
			a,b,c = map(int, line.split())
			if a <= n and b <= n:
				graph[a-1].append((b-1,c))
				graph[b-1].append((a-1,c))
 
q = [(0, 0)]
while q:
	w, node = heappop(q)
	for nodes in graph[node]:
		if dis[nodes[0]] > dis[node]+nodes[1]:
			dis[nodes[0]] = dis[node]+nodes[1]
			parent[nodes[0]] = node
			heappush(q, (dis[nodes[0]], nodes[0]))
 
if parent[n-1] == -1:
	print(-1)
else:
	path = []
	s = n-1
	while s != -1:
		path.append(s+1)
		s = parent[s]
	path.reverse()
	print(*path)
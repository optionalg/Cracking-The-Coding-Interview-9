vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

def bfs(graph, start, end):
	vertexList, edgeList = graph

	visitedList = []
	queue = [start]
	adjacencyList = [[] for vertex in vertexList]
	
	for edge in edgeList:
		adjacencyList[edge[0]].append(edge[1])

	while queue:
		cur = queue.pop()
		for neighbor in adjacencyList[cur]:
		    if neighbor not in visitedList:
				queue.insert(0, neighbor)
		visitedList.append(cur)

	if end in visitedList:
		print True
	else:
		return False
		
	return visitedList

print bfs(graphs, 0, 4)
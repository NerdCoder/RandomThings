#!/usr/bin/python
from __future__ import print_function
import pprint as pp

edges = [ ('a', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'e'), ('c', 'f'), ('d', 'g') ]
adjList = {}
visited = []
limit = 0

def make_list( adjList, X, Y ):
	if X not in adjList:
		adjList[X] = []
	if Y not in adjList:
		adjList[Y] = []
	adjList[X].append(Y)
	adjList[Y].append(X)


def DLS(current_node, depth):
	if depth > limit:
		return
	
	visited.append(current_node)
	print( "Visited:" , current_node, "| Depth:", depth)
	
	for connected_node in adjList[current_node]:
		if connected_node not in visited:
			DLS(connected_node, depth+1)

if __name__ == '__main__':
	for x,y in edges:
		make_list(adjList, x, y)
	
	#pp = PrettyPrinter(indent=2)
	pp.pprint( adjList )
	limit = 2
	
	DLS('a', 0)

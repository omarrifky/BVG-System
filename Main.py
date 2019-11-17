# Reading the data of the stations from a text file
parentPath = "/Users/ziko137/Documents/GitHub/BVG-System/"
stationsTextFile = open(parentPath + "Stations.txt", "r")
uBahnData = stationsTextFile.read()
#data = uBahnData.split(",");
#print(data);
#print(uBahnData)

###############################################
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Node(object):
    #constructor
    def __init__(self,ID):
        self.visited = False
        self.parentNode = None
        self.possibleMoves = []
        self.possibleMovesCost = []
        self.id = ID
        
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(Node) 
        
	# Function to print a BFS of graph 
	def BFS(self,startNode,goalNode): 
		# Create a queue for BFS 
		queue = [] 
        
        
		# Mark the source node as 
		# visited and enqueue it 
		queue.append(startNode)

		goal = Node(-1)
        
		while queue: 
			# Dequeue a vertex from 
			# queue and print it 
			currentNode = queue.pop(0) 
			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			possibleMovesArray = self.graph[currentNode].possibleMoves
			for i in range(0,len(possibleMovesArray)):
				if goalNode == possibleMovesArray[i]:
					goal = self.graph[possibleMovesArray[i]]
					goal.parentNode = self.graph[currentNode]
					queue = []
					break
				if self.graph[possibleMovesArray[i]].visited == False: 
					self.graph[possibleMovesArray[i]].parentNode = self.graph[currentNode]
					queue.append(possibleMovesArray[i]) 
					self.graph[possibleMovesArray[i]].visited = True

		# goal Node now in Goal backtrack to get Path
		#print(goal.id)
		if not(goal.id ==-1):
			pathInverted = []
			while True:
				pathInverted.append(goal)
				if (goal.parentNode is None):
					break
				else:
					goal = goal.parentNode
				
			for x in pathInverted:
				print(x.id)


			

# Driver code 
allStations = []
uBahnData = uBahnData.replace("\n","")
linesSeperated = uBahnData.split("#")

for line in linesSeperated:
	lineSeperated = line.split(",")
	for x in range (0,len(lineSeperated)-1,2):
         if not(allStations.__contains__(lineSeperated[x])):
             allStations.append(lineSeperated[x])
g = Graph()

for j in range(0,len(allStations)-1):
	station = allStations[j]
	stationNode = Node(j)
	for line in linesSeperated:
		lineSeperated = line.split(",")
		for x in range (0,len(lineSeperated)-1):
			if lineSeperated[x] == station:
				if (x + 3) < (len(lineSeperated)-1) and not (stationNode.possibleMoves.__contains__(allStations.index(lineSeperated[x+2]))): 
					cost = int(lineSeperated[x+3]) - int(lineSeperated[x+1])
					stationNode.possibleMoves.append(allStations.index(lineSeperated[x+2]))
					stationNode.possibleMovesCost.append(abs(cost))
				if x > 1 and x+1 < (len(lineSeperated)-1) and not (stationNode.possibleMoves.__contains__(allStations.index(lineSeperated[x-2]))):
					cost = int(lineSeperated[x-1]) - int(lineSeperated[x+1])
					stationNode.possibleMoves.append(allStations.index(lineSeperated[x-2]))
					stationNode.possibleMovesCost.append(abs(cost))
	g.graph[j] = stationNode


print(g.graph[2].possibleMoves)
#g.BFS(0,3)
	

# Create a graph given in 
# the above diagram 
#g = Graph() 
#g.addEdge(0, 1,5) 
#g.addEdge(0, 2,6) 
#g.addEdge(1, 2,7) 
#g.addEdge(2, 0,8) 
#g.addEdge(2, 3,9) 
#g.addEdge(3, 3,10) 








#print ("Following is Breadth First Traversal" " (starting from vertex 2)") 
#g.BFS(2) 

# This code is contributed by Neelam Yadav 

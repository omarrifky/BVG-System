# Reading the data of the stations from a text file
parentPath = "/Users/Omar Rifky/Documents/GitHub/BVG-System/"
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
    def __init__(self):
        visted = False
        parentNode = None
        possibleMoves = []
        possibleMovesCost = []
        
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(Node) 
        
	# function to add an edge to graph 
	def addEdge(self,currentTransition,destinationTransition,costTransition):
            self.graph[currentTransition].possibleMoves.append(destinationTransition)
            self.graph[currentTransition].possibleMovesCost.append(costTransition)

	# Function to print a BFS of graph 
	def BFS(self,startNode,goalNode): 

		# Create a queue for BFS 
		queue = [] 
		# Mark the source node as 
		# visited and enqueue it 
		queue.append(startNode)

		while queue: 
			# Dequeue a vertex from 
			# queue and print it 
			currentNode = queue.pop(0) 
			print (currentNode, end = " ") 

			# Get all adjacent vertices of the 
			# dequeued vertex s. If a adjacent 
			# has not been visited, then mark it 
			# visited and enqueue it 
			possibleMovesArray = self.graph[currentNode].possibleMoves
			for i in possibleMovesArray: 
				if goalNode == possibleMovesArray[i]:
					goal = possibleMovesArray[i]
					queue = []
					break
				if possibleMovesArray[i].visited == False: 
					possibleMovesArray[i].parentNode = currentNode
					queue.append(i) 
					possibleMovesArray[i].visited = True

		# goal Node now in Goal backtrack to get Path

		if goal is None:
			pathInverted = []
			pathInverted.append(goal)
			while True:
				goal = goal.parentNode
				pathInverted.append(goal)
				if(goal == goalNode):
					break


			

# Driver code 
allStations = []
linesSeperated = []
linesSeperated = uBahnData.replace("\n","").split("#")

for line in linesSeperated:
	lineSeperated = line.split(",")
	for x in range (0,len(lineSeperated)-1,2):
         if not(allStations.__contains__(lineSeperated[x])):
             allStations.append(lineSeperated[x])
    		
       

print(len(allStations))
print(allStations)
	

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

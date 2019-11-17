# Reading the data of the stations from a text file
import os.path
stationsTextFile = open(os.path.dirname(__file__)+"/Stations.txt", "r")
uBahnData = stationsTextFile.read()

# Imports
from collections import defaultdict 

# This class represents a Node Object
class Node(object):
    #constructor
    def __init__(self,ID):
        self.visited = False
        self.parentNode = None
        self.possibleMoves = []
        self.possibleMovesCost = []
        self.id = ID
# Graph Class has default dict of Nodes and the Traversals
class Graph: 

	# Constructor 
	def __init__(self): 
		# default dictionary to store graph 
		self.graph = defaultdict(Node) 
	
	#DFS Traversal 
	def DFS(self,startNode,goalNode): 
		# Create a stack for DFS 
		stack = [] 
		#push first startNode to start traversing DFS
		self.graph[startNode].visited = True
		stack.append(startNode)
		# Initialize goal Node
		goal = Node(-1)
        # traversing the stack until its empty
		while stack: 
			# pop an element
			currentNode = stack.pop()
			# check if it is a goal if it is break from the loop goal found
			if int(goalNode) == int(currentNode):
				goal = self.graph[currentNode]
				break
			# Get possible Moves for current Node
			possibleMovesArray = self.graph[currentNode].possibleMoves
			#push every possible move if not visited before
			for possibleMove in possibleMovesArray:
				if self.graph[possibleMove].visited == False: 
					self.graph[possibleMove].parentNode = self.graph[currentNode]
					stack.append(possibleMove) 
					self.graph[possibleMove].visited = True
		#If Goal Found
		if not(goal.id ==-1):
			pathInverted = []
			#Tranverse Parents of Goal Node till start Node is reached and print path
			while not (goal is None):
				print(goal.id)
				pathInverted.append(goal)
				goal = goal.parentNode
				
			for x in pathInverted:
				print(allStations[x.id])

	#BFS Traversal 
	def BFS(self,startNode,goalNode): 
		# Create a queue for BFS 
		queue = [] 
		#enqueue first startNode to start traversing BFS
		self.graph[startNode].visited = True
		queue.append(startNode)
		# Initialize goal Node
		goal = Node(-1)
        # traversing the queue until its empty
		while queue: 
			# Dequeue an element
			currentNode = queue.pop(0)
			# check if it is a goal if it is break from the loop goal found
			if int(goalNode) == int(currentNode):
				goal = self.graph[currentNode]
				break
			# Get possible Moves for current Node
			possibleMovesArray = self.graph[currentNode].possibleMoves
			#Enqueue every possible move if not visited before
			for possibleMove in possibleMovesArray:
				if self.graph[possibleMove].visited == False: 
					self.graph[possibleMove].parentNode = self.graph[currentNode]
					queue.append(possibleMove) 
					self.graph[possibleMove].visited = True
		#If Goal Found
		if not(goal.id ==-1):
			pathInverted = []
			#Tranverse Parents of Goal Node till start Node is reached and print path
			while not (goal is None):
				print(goal.id)
				pathInverted.append(goal)
				goal = goal.parentNode
				
			for x in pathInverted:
				print(allStations[x.id])


			

#Initialize An Array That has all stations (unique) 
allStations = []
#Remove \n from File and put each line in an element in an array
uBahnData = uBahnData.replace("\n","")
linesSeperated = uBahnData.split("#")
#Fill all Stations (each station only occuring once)
for line in linesSeperated:
	lineSeperated = line.split(",")
	for x in range (0,len(lineSeperated)-1,2):
         if not(allStations.__contains__(lineSeperated[x])):
             allStations.append(lineSeperated[x])
#Create Graph
g = Graph()
#Add Edges with cost from each station to station
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

#DEBUGGING
#print(g.graph[1].possibleMoves)
g.DFS(0,100)

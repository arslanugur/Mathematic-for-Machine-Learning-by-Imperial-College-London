# Consider once again our permutations of students in a line. 
# Recall the nodes in the graph represent permutations, and that the edges represent swaps of adjacent students. 
# We want to design a weighted graph, weighting edges higher for moves that are harder to make. 
# Which of these could be easily implemented by simply assigning weights to the edges already in the graph?

# ---> A) A large student who is difficult to move around in line.
# ---> B) A sticky spot on the floor which is difficult to move onto and off of.
# ---  C) A student who resists movement to the back of the line, but accepts movement toward the front.

# Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, as well as the parameters from Edge. 
# You should additionally include a getWeight method. 
# The string value of a WeightedEdge from node A to B with a weight of 3 should be "A -> B (3)".

# class WeightedEdge(Edge):
#     def __init__(self, src, dest, weight):
#         # Your code here
#         pass
#     def getWeight(self):
#         # Your code here
#         pass
#     def __str__(self):
#         # Your code here
#         pass

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + "->" + str(self.dest) + " (" + str(self.weight) + ")"

# Second Way

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"
        
        
        
        

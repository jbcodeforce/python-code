'''
Created on Apr 26, 2014

implement some graph algo

@author: boyerje
'''


# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved
from collections import deque

class Graph :
    """ Graph has an internal structure mapped as a dictionnary, with vertes and the list of vertex that can be reached
    from that vertex with edge weight.
    {'a': [('b',10),('c',15),('d',7)],....
    """

    def __init__(self):
        self.graph = {}


    def addVertex(self,element):
        self.graph.setdefault(element)
        self.graph[element]=[]

    def addEdge(self,src,dest,w):
        self.graph[src].append((dest,w))
        self.graph[dest].append((src,w))

    def minSpanningTree(self,root):
        """ Compute the minimum spanning tree. A path in the graph going to all nodes by using the less costly edges
        The return structure is a list of vertex in the order of navigation from the root
        """
        result=[root]
        # need to use a queue; to represent the vertex not yet traversed
        queue=deque()
        # add all the elements in a queue
        queue.append(root)
        for e in self.graph.keys() :
            if (e != root) : queue.append(e)

        currentV=root
        queue.popleft()
        while len(queue) > 0 :
            # find neighbour of current vertex connected by the lowest edge weight still in the queue
            min = 100 # maximum weight
            minEdge = None
            for (v,w) in self.graph[currentV] :
                if (v not in queue): continue
                if (w < min) :
                    min = w
                    minEdge=v
            # select the vertex which becomes current and remote it from the queue as we traversed it
            if (minEdge != None) :
                result.append(minEdge)
                currentV=minEdge
                queue.remove(minEdge)
        return result


    def dfs(self,root,elementToSearch=None):
        """ Depth first search: go over the branches of the graph from a root and visit all vertex by going farther from the root
        as possible.
        The return parameter is a list of vertex visited, in their order of visit
        rule 1: add non visited neighbors in a LIFO stack.
        rule 2: when on a vertex with no more neighbor visited then pop one vertex from the stack
        rule 3: when there is no more vertex to traverse the stack is empty
        """
        result=[]
        stack=[root]
        while len(stack) > 0 :
            currentV=stack.pop()
            result.append(currentV)
            # add to stack the current vertex neighbors if not already traversed
            for (v,w) in self.graph[currentV] :
                if v not in result: 
                    stack.append(v)
        return result

    def breadth_first_search(self,root,elementToSearch=None):
        """
        explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
        """
        result = []
        queue=deque([root])
        while queue :
            currentV = queue.popleft()
            result.append(currentV)
            for (v,w) in self.graph[currentV]:
                if v not in result:
                    queue.append(v)
        return result


# ------ tests
# a -> b  4
g=Graph()
g.addVertex('a')
g.addVertex('b')
g.addVertex('h')
g.addVertex('c')
g.addVertex('g')
g.addVertex('i')

g.addEdge('a','b',4)
g.addEdge('a','h',8)
g.addEdge('b','h',11)
g.addEdge('b','c',8)
g.addEdge('c','i',2)
g.addEdge('c','g',4)
g.addEdge('i','h',7)
g.addEdge('i','g',6)
g.addEdge('h','g',1)

print(g.graph)

# compute minimum spanning tree
print("Minimum spanning tree from a:")
r=g.minSpanningTree('a')
print(r)
print("DFS on g from a")
print(g.dfs('a'))
print("BFS on g from a")
print(g.breadth_first_search('a'))


# build a tree
t=Graph()
t.addVertex('25')
t.addVertex('13')
t.addVertex('16')
t.addVertex('18')
t.addVertex('19')
t.addVertex('21')
t.addVertex('23')
t.addVertex('27')
t.addEdge('25','13',1)
t.addEdge('25','16',1)
t.addEdge('13','18',1)
t.addEdge('13','19',1)
t.addEdge('18','21',1)
t.addEdge('18','23',1)
t.addEdge('16','27',1)
print("The tree looks like:")
print(t.graph)
print("Do a depth first search")
r=t.dfs('25')
print(r)
print("Do a breadth first search")
r=t.breadth_first_search('25')
print(r)

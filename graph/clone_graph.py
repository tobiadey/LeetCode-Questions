'''
Question: Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Solution: perform dfs/bfs adding nodes and its neighbours to a hashmap that contains a copy of the node.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: O(v+e) and Space: O(v+e)
# Runtime: 44 ms, faster than 87.18% 
# Memory Usage: 14.4 MB, less than 78.15%

def cloneGraph(node):
    nodes = {}
    
    def dfs(node):
        if node in nodes:
            return nodes[node]

        copy = Node(node.val)
        nodes[node] = copy
        
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    
    return dfs(node) if node else None

INPUT_LIST = [[2,4],[1,3],[2,4],[1,3]]
print(func(INPUT_LIST,K)) #output [[2,4],[1,3],[2,4],[1,3]]

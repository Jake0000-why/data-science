def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsRec(adj, visited, i, res)

def DFS(adj):
    visited = [False] * len(adj)
    res=[]
    dfsRec(adj, visited, 0 ,res)
    return res

def add_edge(adj,s,t):
    adj[s][t]= 1
    adj[t][s]=1

V = 12

adj=[[0]*V for _ in range(V)]

edges = [(1,2), (0,1), (2,0),(2,3),(2,4),(3,5), (4,6) ,(5,7),(6,7),(3,6), (3,8), (3,4)]

for s,t in edges:
    add_edge(adj,s,t)
res = DFS(adj)
print(" ".join(map(str,res)))

def bfs(adj):
    V=len(adj)
    res = []
    s=0
    from collections import deque
    q = deque()

    visited = [False] * V

    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x]=True
                q.append(x)
    return res
adj = [[1,2],[0,2,3],[0,4],[1,4,5],[2,3,5],[4,3]]
ans = bfs(adj)
for i in ans:
    print(i,end=" ")

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

root = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
root.left = node2
root.right = node3
node2.left = node4

def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=" ")
    in_order_dfs(node.right)

def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=" ")

print()
in_order_dfs(root)
print()
pre_order_dfs(root)
print()
post_order_dfs(root)
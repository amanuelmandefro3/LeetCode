class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    edges.append([i, j])
        root = [i for i in range(n)]
        size = [1 for i in range(n)]
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            px = find(x)
            py = find(y)
            if py != px:
                
                if size[px] > size[py]:
                    root[py] = px
                    size[px] += size[py]
                else:
                    root[px] = py
                    size[py] += size[px]
        for x, y in edges:
            union(x,y)
        print(root, edges)    
        parent = set()
        for r in root:
            pr = find(r)
            parent.add(pr)
        return len(parent)    
        
        return len(root)                    


        # graph = {i:[] for i in range(len(isConnected))}

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[0])):
        #         if isConnected[i][j] and i != j:
        #             graph[i].append(j)
              
        # visited = set() 
        # count = 0           
        # # for i in range(len(isConnected)): 
        # #     if i not in visited:
        # #         visited.add(i)            
        # #         stack = [i]
        # #         while stack:
        # #             node = stack.pop()
        # #             for ngb in graph[node]:
        # #                 if ngb not in visited:
        # #                     stack.append(ngb)
        # #                     visited.add(ngb)
        # #         count += 1            
        # def dfs(node):
        #     visited.add(node)
        #     for ngb in graph[node]:
        #         if ngb not in visited:
        #             dfs(ngb)
        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         dfs(i)
        #         count += 1
                            
        # return count           
        
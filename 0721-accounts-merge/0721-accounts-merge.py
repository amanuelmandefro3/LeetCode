class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent, n= {}, len(accounts)
        ans = []
        pos = {}
        ans_val = [set() for _ in range(n)]
        def find(member):
            root = member
            while root != parent[root]:
                root = parent[root]

            while member != root:
                p = parent[member]
                parent[member] = root
                member = p
            return root  

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py


        for i in range(n):
            ans.append(accounts[i][0])
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in parent:
                    parent[accounts[i][j]] = accounts[i][j]
                    pos[accounts[i][j]] = i
            for j in range(1, len(accounts[i])-1):
                union(accounts[i][j], accounts[i][j+1])

        for i in range(n):
            for j in range(1, len(accounts[i])):
                px = find(accounts[i][j])
                idx = pos[px]
                # print(accounts[i][j], )
                ans_val[idx].add(accounts[i][j])     
        
        # print(parent)
        # print(ans_val)
        res = []
        for i in range(n):
            if len( ans_val[i]) > 0:    
                account = [ans[i]]
                emails = list(ans_val[i])
                emails.sort()
                print(emails)
                account.extend(emails)
                res.append(account)
           
        print(res)

        return res              
    
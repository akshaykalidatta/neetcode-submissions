class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst in tickets:
            if src not in adj:
                adj[src] = [dst]
            else:
                adj[src].append(dst)

        for i in adj:
            dsts = adj[i]
            dsts.sort(reverse=True)
            adj[i] = dsts

        ans = []
        def dfs(node):
            while node in adj and len(adj[node])!=0:
                neighs = adj[node]
                dfs(neighs.pop()) 
            ans.append(node)

        dfs('JFK')
        ans.reverse()
        return ans
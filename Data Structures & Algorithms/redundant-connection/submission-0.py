class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        rank = [1]*(len(edges)+1)

        def find(n):
            while parent[n]!=n:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return parent[n]

        def union(src, dst):
            p1, p2 = find(src), find(dst)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            if rank[p1] == rank[p2]:
                parent[p1] = p2
                rank[p2] += 1
            return True
            
        for src, dst in edges:
            if not union(src, dst):
                return [src, dst]

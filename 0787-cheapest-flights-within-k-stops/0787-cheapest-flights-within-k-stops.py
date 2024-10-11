class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

       
        for _ in range(k + 1):
            curr = dist[:]
            for u, v, w in flights:
                if dist[u] != float('inf'): 
                    curr[v] = min(curr[v], dist[u] + w)
            dist = curr[:]

        return dist[dst] if dist[dst] != float('inf') else -1
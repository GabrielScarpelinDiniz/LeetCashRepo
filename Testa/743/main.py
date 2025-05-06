import sys
import heapq
import math

class Solution:

    def networkDelayTime(self, times, n, k) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        
        distances = [math.inf] * n
        distances[k-1] = 0
        visited = [False] * n
        
        heap = [(0, k-1)]
        
        while heap:
            current_dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            
            for v, w in graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    heapq.heappush(heap, (distances[v], v))
        
        max_dist = max(distances)
        return max_dist if max_dist != math.inf else -1

if __name__ == "__main__":
    s = Solution()
    print(s.networkDelayTime([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5))

from collections import defaultdict
import heapq

def dijkstra(graph,start):
    visited=set()
    heap=[[0,start]]
    distances={node:float("inf") for node in graph}
    distances[start]=0
    while heap:
        dist,node=heapq.heappop(heap)
        if node  in visited:
            continue
        visited.add(node)
        for neighbour,weight in graph[node]:
            new_dist=dist+weight
            if new_dist<distances[neighbour]:
                distances[neighbour]=new_dist
                heapq.heappush(heap,(new_dist,neighbour))
    return distances



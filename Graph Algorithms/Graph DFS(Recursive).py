from collections import defaultdict
def RecursiveDFS(graph,start):
    visited=set()
    if start not in visited:
        print(start)
        for neighbor in graph[start]:
            visited.add(start)
            RecursiveDFS(graph,neighbor)
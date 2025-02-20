from collections import defaultdict
def IterativeDFS(graph,start):
    stack=[start]
    visited=set()
    while stack:
        start=stack.pop()
        print(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
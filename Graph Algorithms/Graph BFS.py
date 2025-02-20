from collections import defaultdict,deque
def BFS(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        start=queue.popleft()
        print(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
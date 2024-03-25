from collections import deque

def dfs(G, start, end):
    assert start in G, f"{start} node not in Graph"
    assert end in G, f"{end} node not in Graph"
    
    q = deque([start])
    visited = set()
    path = []

    while q:
        node = q.popleft()
        path.append(node)

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in list(G.adj[node]):
            if neighbor not in visited:
                q.extend(neighbor)





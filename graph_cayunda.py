# Assessment 3.3: Graph Algorithm and Program (BFS and DFS) for "CAYUNDA"

def bfs_graph(graph, start_node):
    visited = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited


def dfs_graph(graph, start_node, visited=None):
    if visited is None:
        visited = []
    visited.append(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited)
    return visited


def main():
    print("========================================")
    print("         GRAPH TRAVERSALS (BFS/DFS)     ")
    print("========================================")

    graph = {
        'C': ['A', 'Y'],
        'A': ['C', 'U', 'N'],
        'Y': ['C', 'U'],
        'U': ['A', 'Y', 'N', 'D'],
        'N': ['A', 'U', 'D'],
        'D': ['U', 'N', 'A']
    }

    start_node = 'C'

    print(f"Starting Node: {start_node}")
    print(f"BFS Traversal: {' -> '.join(bfs_graph(graph, start_node))}")
    print(f"DFS Traversal: {' -> '.join(dfs_graph(graph, start_node))}")


if __name__ == "__main__":
    main()
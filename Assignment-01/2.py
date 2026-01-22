graph = {
    "Raj": ["Sunil"],
    "Priya": ["Raj", "Aarav", "Akash"],
    "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
    "Akash": ["Sunil", "Priya"],
    "Aarav": ["Arjun", "Neha"],
    "Neha": ["Akash", "Aarav", "Raj", "Sneha", "Rahul", "Priya", "Arjun"],
    "Sneha": ["Sunil", "Rahul", "Maya", "Neha"],
    "Rahul": ["Neha", "Sneha", "Maya", "Arjun", "Pooja"],
    "Maya": ["Rahul", "Sunil", "Sneha", "Arjun"],
    "Arjun": ["Rahul", "Pooja", "Maya", "Neha", "Aarav"],
    "Pooja": ["Arjun", "Rahul"]
}

def bfs_tree(graph, start):
    visited=set()
    queue=[start]
    parent={start: None}

    visited.add(start)

    while queue:
        node=queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=node
                queue.append(neighbor)

    return parent

bfs_result=bfs_tree(graph, "Raj")
print("bfs result:")
print(bfs_result)


def dfs_tree(graph, start):
    visited=set()
    parent={start: None}
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor]=node
                dfs(neighbor)

    dfs(start)
    return parent

dfs_result=dfs_tree(graph, "Raj")
print("dfs result:")
print(dfs_result)
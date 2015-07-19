#                       6                     
#          3                         9
#    2           8              3         4
#  1   7      2               6   8


# Depth First Search (DFS)


my_graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def dfs_iterative(graph, start):
    """Depth first search iterative solution"""
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


def dfs_recursive(graph, start, visited=None):
    """Depth first search recursive solution"""
    if visited is None:
        visited = set()
    visited.add(start)
    for node in graph[start] - visited:
        dfs_recursive(graph, node, visited)

    return visited


if __name__ == '__main__':
    # print(depth_first_search(my_graph, 'A'))
    print(my_graph)
    print(dfs_recursive(my_graph, 'A'))

def max_flow(graph, source, sink):

    def bfs(graph, source, sink, parent):

        visited = [False] * len(graph)
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for idx, val in enumerate(graph[u]):
                if not visited[idx] and val > 0:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = u

                    if idx == sink:
                        return True

        return False

    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

graph = [[0, 6, 0, 4, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 0, 0, 4, 0, 0, 5, 0, 0],
         [4, 0, 5, 0, 0, 2, 0, 3, 0, 0],
         [0, 0, 4, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0, 5, 7, 0],
         [0, 0, 0, 0, 4, 0, 0, 3, 4, 2],
         [0, 0, 5, 3, 0, 5, 3, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 4, 7, 0, 1],
         [0, 0, 0, 0, 0, 0, 2, 0, 1, 0]]

source = 0
sink = 9
print("Максимальный поток:", max_flow(graph, source, sink))


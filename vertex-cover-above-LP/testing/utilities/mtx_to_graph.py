def load_mtx_file(filepath):
    edges = set()
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('%'):
                continue
            parts = line.strip().split()
            if len(parts) == 3:
                # First line with dimensions (rows, cols, edges)
                num_vertices = int(parts[0])
            elif len(parts) == 2:
                u, v = int(parts[0]) - 1, int(parts[1]) - 1  # 1-based to 0-based
                if u != v:
                    edge = tuple(sorted((u, v)))
                    edges.add(edge)
    vertices = list(range(num_vertices))
    return vertices, list(edges)
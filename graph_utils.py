import os
from sage.all import Graph


def load_graph(file_name):
    """Load a graph from input_graphs/<file_name>.

    Line 1 = vertex count n; then n lines of `x y neighbor1 neighbor2 ...`.
    """
    G = Graph()
    pos_dict = {}

    with open(os.path.join("input_graphs", file_name), "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])

    for i in range(n):
        parts = lines[i + 1].split()
        pos_dict[i] = (float(parts[0]), float(parts[1]))
        for neighbor in parts[2:]:
            G.add_edge(i, int(neighbor))

    G.set_pos(pos_dict)
    return G

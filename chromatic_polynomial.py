import os
import sys
from sage.all import Graph
from sage.graphs.chrompoly import chromatic_polynomial


def load_graph(file_name):
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


def analyze_graph(file_name):
    G = load_graph(file_name)
    P = chromatic_polynomial(G)
    # Number of proper colorings with exactly the given number of colors
    k_values = [1, 2, 3, 4, 5]
    counts = {k: P(k) for k in k_values}

    # Chromatic number is the smallest k with P(k) > 0
    chromatic_number = next(k for k in range(1, G.order() + 1) if P(k) > 0)

    return G, P, counts, chromatic_number


def main():
    in_dir = "input_graphs"
    out_dir = "out_chromatic_polynomial"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    files = sorted(f for f in os.listdir(in_dir) if f.endswith(".txt"))
    for file_name in files:
        print(f"Processing {file_name} ...")
        G, P, counts, chi = analyze_graph(file_name)
        base = os.path.splitext(file_name)[0]

        lines = [
            f"Graph: {file_name}",
            f"Vertices: {G.order()}",
            f"Edges: {G.size()}",
            f"Chromatic number: {chi}",
            "Chromatic polynomial P(x):",
            str(P),
            "",
            "Proper colorings by number of colors:",
        ]
        lines += [f"  x = {k}: {count}" for k, count in counts.items()]

        report = "\n".join(lines)
        out_path = os.path.join(out_dir, f"{base}_chromatic_polynomial.txt")
        with open(out_path, "w") as f:
            f.write(report + "\n")

        print(report)
        print(f"Saved to {out_path}\n")


if __name__ == "__main__":
    sys.exit(main())

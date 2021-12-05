#!/usr/bin/env python3

import argparse

from five_finder.structs import ChaosHeap
from five_finder.graph import generate_paths

# Graph rendering
import networkx as nx

# UI
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Generate operations needed to get to a target number")
    parser.add_argument("start", type=int, help="Starting number")
    parser.add_argument("target", type=int, help="Target number")
    parser.add_argument("--count", type=int, default=5, help="Number of paths to find")
    parser.add_argument("--print", action="store_true", help="Print path to STDOUT")
    parser.add_argument("--draw", action="store_true", help="Render graph of paths")
    args = parser.parse_args()

    start = args.start
    target = args.target

    less_than = lambda a, b: abs(a[-1][0] - target) < abs(b[-1][0] - target)
    #less_than = lambda a, b: abs(a - target) < abs(b - target)
    q = ChaosHeap(less_than=less_than)

    ops = [mod, add, div, multi, sub]
    gen = generate_paths(start=start, target=target, q=q, operations=ops)
    paths = [next(gen) for _ in range(args.count)]

    if args.print:
        print_paths(paths)

    if args.draw:
        draw(paths)

def print_paths(paths):
    for path in paths:
        print(path)

def draw(paths):
    g = nx.DiGraph()

    labels = {}
    for path in paths:
        for idx, node in enumerate(path[:-1]):
            next_node = path[idx + 1]
            edge = (node[0], next_node[0])
            labels[edge] = node[1]
            g.add_edge(*edge)

    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw(g, pos, node_color="pink", labels={node: node for node in g.nodes()})
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, font_color="black")
    plt.axis("off")
    plt.show()

def mod(a, b):
    if b == 0:
        return (None, None)

    return (a % b, "%")

def add(a, b):
    return (a + b, "+")

def div(a, b):
    if b == 0 or a % b != 0:
        return (None, None)

    return (a // b, "/")

def multi(a, b):
    return (a * b, f"*")

def sub(a, b):
    return (a - b, f"-")

if __name__ == "__main__":
    main()
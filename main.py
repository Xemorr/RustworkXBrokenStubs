# This is a sample Python script.
from typing import Dict

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import rustworkx


def print_hi(name: str) -> rustworkx.AllPairsPathLengthMapping:
    # Use a breakpoint in the code line below to debug your script.
    graph: rustworkx.PyDiGraph = rustworkx.PyDiGraph()
    graph.add_node(6)
    graph.add_node(5)
    return rustworkx.digraph_all_pairs_dijkstra_path_lengths(graph, [0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

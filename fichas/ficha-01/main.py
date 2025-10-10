
from Graph import Graph

def menu():
    print("----- Graphs -----")
    print("[1] - Show graph")
    print("[2] - Draw graph")
    print("[3] - Show nodes")
    print("[4] - Depth-First Search")
    print("[5] - Breadth-First Search")
    print("[0] - Exit")


def main():

    g1 = Graph(False)
    g1.add_edge("s", "a", 2)
    g1.add_edge("a", "b", 2)
    g1.add_edge("b", "c", 2)
    g1.add_edge("c", "d", 3)
    g1.add_edge("d", "t", 3)
    g1.add_edge("t", "g", 2)
    g1.add_edge("g", "f", 2)
    g1.add_edge("f", "e", 5)
    g1.add_edge("e", "s", 2)

    print(g1.edges)

    out = -1
    while out != 0:
        menu()
        out = int(input("option: "))

        if out == 0:
            print("leaving...")
        elif out == 1:
            print(g1)
            input("press enter to continue")
        elif out == 2:
            g1.draw()
        elif out == 3:
            print("nodes: ", g1.get_nodes())
            input("press enter to continue")
        elif out == 4:
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g1.depth_first_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g1.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        elif out == 5:
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g1.breadth_first_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g1.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        else:
            print("invalid choice!")
            input("press enter to continue")


if __name__ == "__main__":
    main()
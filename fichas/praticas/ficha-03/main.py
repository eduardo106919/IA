
from Buckets import Buckets
from Graph import Graph

def menu():
    print("----- Graphs -----")
    print("[1] - Show graph")
    print("[2] - Draw graph")
    print("[3] - Show nodes")
    print("[4] - Depth-First Search")
    print("[5] - Breadth-First Search")
    # print("[6] - Greedy Search")
    # print("[7] - A* Search")
    print("[0] - Exit")


def main():
    b : Buckets = Buckets(bucket1_cap=4, bucket2_cap=3)

    b.create_graph()
    g : Graph = b.get_graph()

    b.set_goal((0,2))
    # b.set_goal((2,0))

    print((0,2))

    out = -1
    while out != 0:
        menu()
        out = int(input("option: "))

        if out == 0:
            print("leaving...")
        elif out == 1:
            print(g)
            input("press enter to continue")
        elif out == 2:
            g.draw()
        elif out == 3:
            print("nodes: ", g.get_nodes())
            input("press enter to continue")
        elif out == 4:
            print("source node: " + str(b.get_start()))
            print("destiny node: " + str(b.get_goal()))
            path = list()
            visited = set()

            print("found: ", g.depth_first_search(str(b.get_start()), str(b.get_goal()), path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        elif out == 5:
            print("source node: " + str(b.get_start()))
            print("destiny node: " + str(b.get_goal()))
            path = list()
            visited = set()

            print("found: ", g.breadth_first_search(str(b.get_start()), str(b.get_goal()), path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        else:
            print("invalid choice!")
            input("press enter to continue")


if __name__ == "__main__":
    main()

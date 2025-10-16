
from Graph import Graph

def menu():
    print("----- Graphs -----")
    print("[1] - Show graph")
    print("[2] - Draw graph")
    print("[3] - Show nodes")
    print("[4] - Depth-First Search")
    print("[5] - Breadth-First Search")
    print("[6] - Greedy Search")
    print("[7] - A* Search")
    print("[0] - Exit")


def main():

    g = Graph()

    g.add_edge("elvas", "borba", 15)
    g.add_edge("borba", "estremoz", 15)
    g.add_edge("estremoz", "evora", 40)
    g.add_edge("evora", "montemor", 20)
    g.add_edge("montemor", "vendasnovas", 15)
    g.add_edge("vendasnovas", "lisboa", 50)
    g.add_edge("elvas", "arraiolos", 50)
    g.add_edge("arraiolos", "alcacer", 90)
    g.add_edge("alcacer", "palmela", 35)
    g.add_edge("palmela", "almada", 25)
    g.add_edge("palmela", "barreiro", 25)
    g.add_edge("barreiro", "palmela", 30)
    g.add_edge("almada", "lisboa", 15)
    g.add_edge("elvas", "alandroal", 40)
    g.add_edge("alandroal", "redondo", 25)
    g.add_edge("redondo", "monsaraz", 30)
    g.add_edge("monsaraz", "barreiro", 120)
    g.add_edge("barreiro", "baixadabanheira", 5)
    g.add_edge("baixadabanheira", "moita", 7)
    g.add_edge("moita", "alcochete", 20)
    g.add_edge("alcochete", "lisboa", 20)

    g.add_heuristic("elvas", 270)
    g.add_heuristic("borba", 250)
    g.add_heuristic("estremoz", 145)
    g.add_heuristic("evora", 95)
    g.add_heuristic("montemor", 70)
    g.add_heuristic("vendasnovas", 45)
    g.add_heuristic("arraiolos", 220)
    g.add_heuristic("alcacer", 140)
    g.add_heuristic("palmela", 85)
    g.add_heuristic("almada", 25)
    g.add_heuristic("alandroal", 180)
    g.add_heuristic("redondo", 170)
    g.add_heuristic("monsaraz", 120)
    g.add_heuristic("barreiro", 30)
    g.add_heuristic("baixadabanheira", 33)
    g.add_heuristic("moita", 35)
    g.add_heuristic("alcochete", 26)
    g.add_heuristic("lisboa", 0)

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
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g.depth_first_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        elif out == 5:
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g.breadth_first_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        elif out == 6:
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g.greedy_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        elif out == 7:
            start = input("source node: ")
            end = input("destiny node: ")
            path = list()
            visited = set()

            print("found: ", g.a_star_search(start, end, path, visited))
            print("path: ", path)
            print("path cost: ", g.get_path_cost(path))
            print("visited: ", visited)
            input("press enter to continue")
        else:
            print("invalid choice!")
            input("press enter to continue")


if __name__ == "__main__":
    main()

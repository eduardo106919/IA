
from Graph import Graph
from Node import Node


def main():

    #add nodes and connections

    g = Graph(False)
    g.add_edge("s", "a", 2)
    g.add_edge("a", "b", 2)
    g.add_edge("b", "c", 2)
    g.add_edge("c", "d", 3)
    g.add_edge("d", "t", 3)
    g.add_edge("t", "g", 2)
    g.add_edge("g", "f", 2)
    g.add_edge("f", "e", 5)
    g.add_edge("e", "s", 2)

    '''
    g = Graph(True)
    g.add_edge("1", "2", 1)
    g.add_edge("1", "3", 2)
    g.add_edge("3", "4", 1)
    g.add_edge("4", "1", 3)
    g.add_edge("4", "5", 4)
    g.add_edge("5", "6", 2)
    g.add_edge("6", "4", 1)
    g.add_edge("5", "7", 2)
    '''

    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-DFS")
        print("6-BFS")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(g.m_graph)
            l = input("prima enter para continuar")
        elif saida == 2:
            g.desenha()
        elif saida == 3:
            print(g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            path = []
            visited = set()
            print(g.procura_DFS(inicio, fim, path, visited))
            print("path: ")
            print(path)
            print("visited: ")
            print(visited)
            l = input("prima enter para continuar")
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            path = []
            visited = set()
            print("Encontrou: ", g.procura_BFS(inicio, fim, path, visited))
            print("path: ")
            print(path)
            print("visited: ")
            print(visited)
            l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()

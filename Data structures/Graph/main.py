from Grafo import Grafo
from queue import Queue


def BFS(G, s):
    V = G.getNodes()
    V[s].setColor("GRAY")
    V[s].setDistance(0)

    Q = Queue()
    Q.put(V[s])
    while not Q.empty():
        u = Q.get()
        AS = G.adj(u.getId())
        # for v in AS:


if __name__ == "__main__":
    G = Grafo()
    G.crear_lista("Data structures/Graph/BP/tinyEWG.txt")
    G.show()
    BFS(G, 0)

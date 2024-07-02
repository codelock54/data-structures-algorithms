from Nodo import Nodo
class Grafo:
    def __init__(self):
        self.L = [] #donde almacenara la lista de adyacencia
        self.V = None #Lista de nodos
    def getNodes(self):
        return self.V
    def show(self):
        n = len(self.L)
        for i in range(n):
            print(self.L[i])
            
    def crear_lista(self,path):
        f = open(path)
        v = int(f.readline())
        e = int(f.readline())
    
        self.V = [ Nodo(i) for i in range(v)]
        
        self.L = [[] for _ in range(v)]
        
        for _ in range(e):
            linea = f.readline().split()
            a = int(linea[0])
            b = int(linea[1])
            w = float(linea[2])
            self.L[a].append(b)
        
    def adj(self,u_id):
        return self.L[u_id]

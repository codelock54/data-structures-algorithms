def mostrar_matriz(M):
    n = len(M)
    for i in range(n):
        print(M[i])
        
def crear_matriz(path):
    f = open(path)
    v = int(f.readline())
    e = int(f.readline())
    
    M = [[0.0 for _ in range(v)] for _ in range(v)]
    for _ in range(e):
        linea = f.readline().split()
        a = int(linea[0])
        b = int(linea[1])
        w = float(linea[2])
        M[a][b] = w
    return M

G = crear_matriz("tinyEWG.txt")
mostrar_matriz(G)
#print(G)
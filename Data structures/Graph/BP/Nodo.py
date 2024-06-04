class Nodo:
    def __init__(self,id):
        self.id = id
        self.d = float('inf')
        self.color = 'WHITE'
        self.dad = float('inf')
    def setId(self,idx):
        self.id = idx
    def getId(self):
        return self.id
    def setDistance(self, dist):
        self.d = dist
    def getDistance(self):
        return self.d
    def setColor(self,col):
        self.color = col
    def getColor(self):
        return self.color
    def setDaddy(self,idad):
        self.dad = idad
    def getDaddy(self):
        return self.dad
    def __str__(self):
        return str(self.id)+": "+self.color
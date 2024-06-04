class node():

    def __init__(self, id):
        self.id = id
        self.color = 'WHITE'
        self.distance = float('inf')
        self.dad = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setColor(self, color): 
        self.color = color

    def getColor(self):
        return self.color
    
    def setDistance(self, distance): 
        self.distance = distance

    def getDistance(self):
        return self.distance
         
    def setDad(self, dad): 
        self.dad = dad

    def getDad(self):
        return self.dad

    def __str__(self):
        return str (self.id) + ": "+str(self.distance) + " "+str(self.color) +" "+str(self.dad)+" "
    
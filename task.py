class Container:
    def __init__(self):
        self.amount = 0.0
        self.neighbors = set()
        self.group = {self}
    def getAmount(self):
        return self.amount
    def setGroup(self,group):
        for c in group:
            c.group= group
    def recomputeComp(self):
        visited = set()
        stack = [self]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(node.neighbors)
        total = sum(c.amount for c in visited)
        share = total/len(visited)
        for c in visited:
            c.amount = share
        self.setGroup(visited)
    def connectTo(self,other):
        if other in self.neighbors:
            return
        self.neighbors.add(other)
        other.neighbors.add(self)
        self.recomputeComp()
    def disconnectFrom(self,other):
        if other not in self.neighbors:
            return
        self.neighbors.remove(other)
        other.neighbors.remove(self)
        self.recomputeComp()
        other.recomputeComp()
    def addWater(self,a):
        component = self.group 
        total = sum(c.amount for c in component)+a
        share = total/len(component)
        for c in component:
            c.amount = share 

a = Container()
b = Container()
c = Container()
a.addWater(12)
b.addWater(6)
a.connectTo(b)     
print(a.getAmount(), b.getAmount())  
b.connectTo(c)      
print(a.getAmount(), b.getAmount(), c.getAmount())  
b.disconnectFrom(c) 
print(a.getAmount(), b.getAmount())  
print(c.getAmount())                 

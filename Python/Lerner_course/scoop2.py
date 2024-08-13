import pickle

class Scoop(object):
    
    def __init__(self, flavor, size="Medium", container="Cup"):
        self.flavor = flavor
        self.size = size
        self.container = container
        
class Bowl(object):
    def __init__(self, scoops):
        self.scoops = scoops
        scoops = [ ]               

    def add_scoops(self, *args):
        scoops += args

    def flavors(self):
        return ", ".join([one_scoop.flavor for one_scoop in self.scoops])
        
s1 = Scoop('Chocolate', "Small", "Cone")
s2 = Scoop('Vanilla')
s3 = Scoop('Coffee')

b = Bowl([s1, s2])
b.scoops
b.flavors

for scoop in b.scoops:
    print(scoop.flavor)